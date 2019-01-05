# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "merias"
app_title = "Merias"
app_publisher = "ahmadragheb"
app_description = "simple custoization to merias co"
app_icon = "octicon octicon-file-directory"
app_color = "pink"
app_email = "ahmedragheb75@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/merias/css/merias.css"
# app_include_js = "/assets/merias/js/merias.js"

# include js, css files in header of web template
# web_include_css = "/assets/merias/css/merias.css"
# web_include_js = "/assets/merias/js/merias.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
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
# get_website_user_home_page = "merias.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "merias.install.before_install"
# after_install = "merias.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "merias.notifications.get_notification_config"

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

doc_events = {
	"Sales Order": {
		"on_update": "merias.api.check_availability_for_items_based_on_booked",
		# "on_submit": "merias.api.check_availability_for_items",
	},"Sales Invoice": {
		# "on_update": "merias.api.si_for_items_based_on_booked",
		"on_submit": "merias.api.si_for_items_based_on_booked",
		# "on_submit": "merias.api.check_availability_for_items",
	# },"Delivery Note": {
	# 	"on_submit": "merias.api.check_availability_for_items_based_on_booked",
	},"Stock Entry": {
		"on_submit": "merias.api.stock_entry",
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"merias.tasks.all"
# 	],
# 	"daily": [
# 		"merias.tasks.daily"
# 	],
# 	"hourly": [
# 		"merias.tasks.hourly"
# 	],
# 	"weekly": [
# 		"merias.tasks.weekly"
# 	]
# 	"monthly": [
# 		"merias.tasks.monthly"
# 	]
# }
scheduler_events = {
	# "all": [
	# 	"merias.tasks.all"
	# ],
	# "daily": [
	# 	"merias.tasks.daily"
	# ],
	"hourly": [
		"merias.tasks.hourly"
	],
	# "weekly": [
	# 	"merias.tasks.weekly"
	# ]
	# "monthly": [
	# 	"merias.tasks.monthly"
	# ]
}

# Testing
# -------

# before_tests = "merias.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "merias.event.get_events"
# }	

fixtures = ["Custom Script","Custom Field"]