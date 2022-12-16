from django.contrib import admin
from website.models import Payments, Settings


@admin.register(Payments)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "cost", "create_at", "complete",)
    search_fields = ["id", "first_name"]


@admin.register(Settings)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "notif_text", "terms_of_use_text", "privacy_policy_text", "description_of_goods_text",
                    "contacts_text",)
    search_fields = ["id", "notif_text", "terms_of_use_text", "privacy_policy_text", "description_of_goods_text",
                     "contacts_text"]