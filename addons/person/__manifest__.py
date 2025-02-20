{
    "name": "Person Management",
    "version": "16.0.1.0.0",
    "category": "Website",
    "summary": "Manage people with website integration",
    "description": """
        Module for managing people, their details, and displaying them on the website.
    """,
    "depends": ["website"],
    "data": [
        "security/ir.model.access.csv",
        "views/persons_views.xml",
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
