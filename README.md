# Test task for the position of Odoo Fullstack Developer

## General description
You need to develop a custom module for Odoo 16 that depends on the `website` module. The task consists of three parts:
1. **Backend**: Creating a model and admin interface.
2. **Frontend**: Displaying data on the website.
3. **Web Client**: Implementation of the form for adding records.

**Module path**: addons/person.

---

## Part 1: Backend
### Model `person`
**Model fields**:
- `first_name` (Text, required) – Name.
- `last_name` (Text, required) – Surname.
- `full_name` (Compute) – concatenation of `first_name` and `last_name` separated by a space.
- `birthday` (Date) – date of birth.
- `age` (Compute) – is calculated based on `birthday`.
- `sex` (Selection) – selection from values: `male`, `female`, `non-binary`.
- `company_id` (Many2one, required) – a reference to `res.company`. The default value is the user's current company.

<img width="1545" alt="Image" src="https://github.com/user-attachments/assets/29329298-1091-48a0-a227-37788dfe6551" />

### Interface requirements
- **List View**: Display `full_name`, `sex`, `age`, `company_id`.
- **Form View**: Allow editing of all fields.
- **Menu**: Add the “Persons” item to the menu of the Website application.

<img width="1427" alt="Image" src="https://github.com/user-attachments/assets/0e41973a-5932-4c9c-84da-3696e3ff1ebb" />

<img width="2560" alt="Image" src="https://github.com/user-attachments/assets/361fddd8-4690-420d-95c1-b6eb8d1b6d37" />

<img width="303" alt="Image" src="https://github.com/user-attachments/assets/502f0f8c-f436-48f9-af98-7b8bf90dba09" />

---

## Part 2: Frontend
### Controller for a website
- **URL**: `/persons`.
- **Template**: Displays the last 5 records of the `person` model in the form of cards.
- **Card fields**:
  - `full_name`
  - `sex` 
  - `age`
  - `company_name`


<img width="682" alt="Image" src="https://github.com/user-attachments/assets/17bc8d0b-e9be-4f87-8e67-7f11ece16740" />

---

## Part 3: Web client
### Form for adding records
- **Realization**: Separate page(`/persons/create_form/`).
- **Form fields**:
  - `first_name`
  - `last_name`
  - `birthday`
  - `sex`
  - `company_id`
- **Processing**: Save data to the `person` model using a POST request.

<img width="2553" alt="Image" src="https://github.com/user-attachments/assets/7eca7ab6-45d4-40ca-a910-5716a49cae2d" />

<img width="519" alt="Image" src="https://github.com/user-attachments/assets/99403785-74a3-43c7-b5c8-511ec05c4e41" />


---

[![Build Status](https://runbot.odoo.com/runbot/badge/flat/1/master.svg)](https://runbot.odoo.com/runbot)
[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/16.0)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](https://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](https://nightly.odoo.com/)

Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>,
<a href="https://www.odoo.com/app/website">Website Builder</a>,
<a href="https://www.odoo.com/app/ecommerce">eCommerce</a>,
<a href="https://www.odoo.com/app/inventory">Warehouse Management</a>,
<a href="https://www.odoo.com/app/project">Project Management</a>,
<a href="https://www.odoo.com/app/accounting">Billing &amp; Accounting</a>,
<a href="https://www.odoo.com/app/point-of-sale-shop">Point of Sale</a>,
<a href="https://www.odoo.com/app/employees">Human Resources</a>,
<a href="https://www.odoo.com/app/social-marketing">Marketing</a>,
<a href="https://www.odoo.com/app/manufacturing">Manufacturing</a>,
<a href="https://www.odoo.com/">...</a>

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.

Getting started with Odoo
-------------------------

For a standard installation please follow the <a href="https://www.odoo.com/documentation/16.0/administration/install/install.html">Setup instructions</a>
from the documentation.

To learn the software, we recommend the <a href="https://www.odoo.com/slides">Odoo eLearning</a>, or <a href="https://www.odoo.com/page/scale-up-business-game">Scale-up</a>, the <a href="https://www.odoo.com/page/scale-up-business-game">business game</a>. Developers can start with <a href="https://www.odoo.com/documentation/16.0/developer/howtos.html">the developer tutorials</a>
