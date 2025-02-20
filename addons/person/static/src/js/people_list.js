document.addEventListener("DOMContentLoaded", function () {
  fetch("/persons/data/", {
    method: "GET",
    headers: {
      Accept: "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      const container = document.querySelector(".person-list");
      data.forEach((person) => {
        const card = document.createElement("div");
        card.innerHTML = `<li class="person-item">
          <h3 class="card-title">${person.full_name}</h3>
          <p class="card-text">
            ${person.sex ? `Sex: ${person.sex}<br />` : ""} ${
          person.age
            ? `Age:
            ${person.age}<br />`
            : ""
        } Company: ${person.company}
          </p>
        </li>`;
        container.appendChild(card);
      });
    })
    .catch((error) => console.error("Error fetching data:", error));
});

