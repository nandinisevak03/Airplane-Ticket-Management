# Copyright (c) 2024, Nandini and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FlightPassenger(Document):
     def validate(self):
        # Ensure that at least one of the names is provided
        if not self.first_name and not self.last_name:
            raise frappe.ValidationError("At least one of First Name or Last Name must be provided.")
        
        # Combine First Name and Last Name to form Full Name
        if self.first_name and self.last_name:
            self.full_name = f"{self.first_name} {self.last_name}"
        elif self.first_name:
            self.full_name = self.first_name
        else:
            self.full_name = "Unknown"  # You can customize this as needed
