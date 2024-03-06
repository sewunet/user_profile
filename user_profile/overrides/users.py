import frappe
from frappe.desk.notifications import clear_notifications
from frappe.core.doctype.user.user import User


class UserEnabled(User):

    def on_update(self):
        quota = frappe.get_site_config()['quota']
        allowed_users = quota["users"]
        active_users = quota['active_users']
         if self.allowed_users < self.active_users:
                frappe.throw('Only {} active users allowed and you have {} active users. Please disable users or to increase the limit please contact sales'. format(allowed_users, active_users))
		# # clear new password
		# super().share_with_self()
		# clear_notifications(user=super().name)
		# frappe.clear_cache(user=super().name)
		# now = frappe.flags.in_test or frappe.flags.in_install
		# super().send_password_notification(super().__new_password)
		# frappe.enqueue(
		# 	"frappe.core.doctype.user.user.create_contact",
		# 	user=super(),
		# 	ignore_mandatory=True,
		# 	now=now,
		# 	enqueue_after_commit=True,
		# )

		# if super().name not in STANDARD_USERS and not super().user_image:
		# 	frappe.enqueue(
		# 		"frappe.core.doctype.user.user.update_gravatar",
		# 		name=super().name,
		# 		now=now,
		# 		enqueue_after_commit=True,
		# 	)

		# # Set user selected timezone
		# if super().time_zone:
		# 	frappe.defaults.set_default("time_zone", super().time_zone, super().name)

		# if super().has_value_changed("enabled"):
           
        #     else:
        #         frappe.cache.delete_key("users_for_mentions")
        #         frappe.cache.delete_key("enabled_users")
		# elif super().has_value_changed("allow_in_mentions") or super().has_value_changed("user_type"):
		# 	frappe.cache.delete_key("users_for_mentions")