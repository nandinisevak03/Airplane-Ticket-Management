# Copyright (c) 2024, Nandini and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random

class AirplaneTicket(Document):
    def before_insert(self):
        number = random.randint(10, 99)
        letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        self.seat = f"{number}{letter}"

    def validate(self):
        addon_items = []
        for addon in self.add_ons:
            if addon.item in addon_items:
                frappe.throw("Duplicate Add-ons are not allowed")
            addon_items.append(addon.item)

        addon_total = 0
        for addon in self.add_ons:
            addon_total += addon.amount
        self.total_amount = int(self.flight_price) + addon_total
        
    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("You cannot submit this ticket because the flight is not boarded.")

    
    def validate(self):
    
        airplane_flight = frappe.get_doc('Airplane Flight', self.flight)
        
     
        airplane = frappe.get_doc('Airplane', airplane_flight.airplane)
        
        
        airplane_capacity = airplane.capacity

      
        booked_tickets = frappe.db.count('Airplane Ticket', {
            'flight': self.flight
        })

       
        if booked_tickets >= airplane_capacity:
            frappe.throw(f"No more tickets can be booked for this flight. The airplane has only {airplane_capacity} seats.")        