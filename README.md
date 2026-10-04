# TaskFlow - Modern Django To-Do List Web Application

A full-featured, responsive To-Do List web application built with Python and Django.

---

## 🚀 How to Run the App

1. **Open your terminal / command prompt** inside this directory (`c:\Users\HP SUREBOOK\Desktop\list`).
2. *(Optional - if Django is not yet installed)*:
   ```bash
   pip install django
   ```
3. **Start the server:**
   ```bash
   python manage.py runserver
   ```
4. **Open in browser:**
   Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

> **Note**: `manage.py` is configured to automatically run database migrations on server start, so you can immediately begin creating and managing tasks!

---

## ✨ Features

- **Task Management**: Create, view, edit, toggle completion, and delete tasks.
- **Priority Levels**: Tag tasks as High, Medium, or Low with color-coded badges.
- **Categories**: Organize tasks by Work, Personal, Study, Shopping, Health, and General.
- **Due Dates & Overdue Alerts**: Set due dates with dynamic badges for "Overdue", "Due Today", and future dates.
- **Live Search & Filters**:
  - Full-text search by title or description
  - Filter by status (`All`, `Active`, `Completed`)
  - Filter by category pills
- **Bulk Action**: One-click "Clear completed" to clean up finished items.
- **Metrics Dashboard**: Real-time counter cards for Total, In Progress, Completed, and Overdue tasks.
- **Responsive & Modern UI**: Built with Tailwind CSS and Font Awesome for desktop and mobile devices.
- **Django Admin**: Access full management at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
