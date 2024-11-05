// Copyright (c) 2024, Nandini and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airline", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        // Check if the website field is not empty
        if (frm.doc.website) {
            // Add a web link to the website field
            frm.add_web_link(__('Visit Website'), frm.doc.website);
        }
    }
});
