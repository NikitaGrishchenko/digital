DEFAULT_APPS = [
    "admin_interface",
    "colorfield",
    "extra_settings",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "import_export",
    "corsheaders",
    "modeltranslation",
    "widget_tweaks",
    "rest_framework",
    # "rest_framework.authtoken",
    "drf_yasg",
    "django_cleanup.apps.CleanupConfig",
    "etc",
    "service_objects",
    "ckeditor",
    "ckeditor_uploader",
    "django_filters",
    # "dj_rest_auth",
]

PROJECT_APPS = [
    "apps.core.utils",
    "apps.core.main",
    "apps.core.api",
    "apps.api.auth",
    "apps.api.article",
    "apps.api.project",
    "apps.api.feedback",
    "apps.api.captcha_test",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
    "django_extensions",
    "debug_toolbar",
]

PRODUCTION_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
]
