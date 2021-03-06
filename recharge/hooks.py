# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "recharge"
app_title = "Recharge"
app_publisher = "Aakvatech"
app_description = "Recharge Distribution Company"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@aakvatech.com"
app_license = "MIT"

fixtures = [
	{"doctype":"Property Setter", "filters": [["name", "in", (
        "Sales Invoice-default_print_format",
        "Sales Invoice Item-rate-columns",
        "Sales Invoice Item-item_code-columns",
        "Sales Invoice Item-warehouse-columns",
        "Sales Invoice Item-qty-columns",
        "Sales Invoice Item-target_warehouse-in_list_view",
        "Sales Invoice-update_stock-default",
        "Purchase Invoice-default_print_format",
        "Purchase Invoice Item-warehouse-columns",
        "Purchase Invoice Item-warehouse-in_list_view",
        "Purchase Invoice-update_stock-default",
        "Purchase Receipt Item-net_amount-columns",
        "Purchase Receipt Item-batch_no-in_list_view",
        "Purchase Receipt Item-serial_no-in_list_view",
        "Purchase Receipt Item-warehouse-columns",
        "Purchase Receipt Item-item_code-columns",
        "Purchase Receipt Item-net_amount-in_list_view",
        "Purchase Receipt Item-amount-in_list_view",
        "Purchase Receipt Item-rate-columns",
        "Purchase Receipt Item-qty-columns",
        "Item-valuation_method-default"
    )]]},
    {"doctype":"Custom Field", "filters": [["name", "in", (
        "Sales Invoice Item-start_series",
        "Sales Invoice Item-end_series",
        "Purchase Receipt Item-start_series",
        "Purchase Receipt Item-end_series",
        "Purchase Invoice Item-end_series",
        "Purchase Invoice Item-start_series",
        "Stock Entry Detail-end_series",
        "Stock Entry Detail-start_series",
        "Purchase Invoice-actual_supplier_invoice_no",
        "Purchase Invoice-actual_supplier_invoice_date"
    )]]},
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/recharge/css/recharge.css"
# app_include_js = "/assets/recharge/js/recharge.js"

# include js, css files in header of web template
# web_include_css = "/assets/recharge/css/recharge.css"
# web_include_js = "/assets/recharge/js/recharge.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_list_js = {
    "Purchase Invoice" : "recharge/purchase_invoice.js",
    "Purchase Receipt" : "recharge/purchase_invoice.js",
    "Stock Entry" : "recharge/stock_entry.js",
    "Sales Invoice" : "recharge/sales_invoice.js",
}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "recharge.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "recharge.install.before_install"
# after_install = "recharge.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "recharge.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"recharge.tasks.all"
# 	],
# 	"daily": [
# 		"recharge.tasks.daily"
# 	],
# 	"hourly": [
# 		"recharge.tasks.hourly"
# 	],
# 	"weekly": [
# 		"recharge.tasks.weekly"
# 	]
# 	"monthly": [
# 		"recharge.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "recharge.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "recharge.event.get_events"
# }

