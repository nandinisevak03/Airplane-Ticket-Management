# Copyright (c) 2024, Nandini and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        # Submit ke baad status 'Completed' set karna
        self.status = 'Completed'
    
    def get_context(self, context):
        # Check if the flight is published
        if self.status != 'Published':
            # Render a custom not found page
            context.message = "This flight is not published yet."
            context.http_status_code = 404  # Set the HTTP status code to 404
            return context  # Return context to render the page
        
        # If published, set up the context as usual
        context.title = self.title  # Example: Set the page title to the flight title
        context.status = self.status  # Pass the status to the web page context
        
        return context  # Return context for rendering the web page
    
    def validate(self):
        # Basic validation to ensure status is valid
        if self.status not in ["Scheduled", "Completed", "Published"]:
            frappe.throw("Invalid status for the Airplane Flight.")
    
    def before_publish(self):
        # Ensure the flight is ready for publishing
        if self.status != 'Published':
            frappe.throw("Flight cannot be published without setting status to Published.")
