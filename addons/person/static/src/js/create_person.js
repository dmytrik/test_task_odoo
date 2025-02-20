document.addEventListener("DOMContentLoaded", function () {
  fetch("/api/companies/", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      const companySelect = document.getElementById("company_id");
      if (data.result && Array.isArray(data.result)) {
        data.result.forEach((company) => {
          const option = document.createElement("option");
          option.value = company.id;
          option.textContent = company.name;
          companySelect.appendChild(option);
        });
      } else {
        console.error("No valid result in response:", data);
      }
    })
    .catch((error) => console.error("Error loading companies:", error));

  const form = document.getElementById("personForm");
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(form);
    const data = {
      first_name: formData.get("first_name"),
      last_name: formData.get("last_name"),
      birthday: formData.get("birthday") || null,
      sex: formData.get("sex") || null,
      company_id: formData.get("company_id"),
    };

    console.log(data);

    fetch("/person/create/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (!response.ok) {
          throw response;
        }
        return response.json();
      })
      .then((data) => {
        showMessage("Person created successfully!", true);
        form.reset();
      })
      .catch((error) => {
        error.json().then((errorData) => {
          showMessage(errorData.error || "An error occurred", false);
        });
      });
  });

  function showMessage(message, isSuccess) {
    const messageDiv = document.getElementById("message");
    messageDiv.textContent = message;
    messageDiv.className = isSuccess ? "success" : "error";

    messageDiv.style.display = "block";
    setTimeout(() => {
      messageDiv.style.opacity = "1";
    }, 10);

    setTimeout(() => {
      messageDiv.style.opacity = "0";
      setTimeout(() => {
        messageDiv.style.display = "none";
      }, 500);
    }, 3000);
  }
});

