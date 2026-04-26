# Leads Management System

This repository now includes a system to manage and export customer leads captured from the collection page pop-up.

## How it works

1.  **Capture**: When a user visits the collection page, a pop-up asks for their email and phone number. This data is stored in the browser's `localStorage`.
2.  **Admin Dashboard**: You can view all captured leads by logging into the admin dashboard (`admin-login.html`).
3.  **Export**: In the "Customer Leads" section of the admin dashboard, there is now an **"Export to Excel"** button. Clicking this will download a `.csv` file (compatible with Excel) containing all current leads.

## Advanced: Syncing to GitHub

If you want to maintain a permanent record in this repository:

1.  Export the leads as `leads.json` from the dashboard (if you implement the JSON export) or manually create a `leads.json` file in the root directory with the following format:
    ```json
    [
      {"email": "user@example.com", "phone": "1234567890", "timestamp": "2026-04-26T12:00:00Z"}
    ]
    ```
2.  Run the provided Python script to generate a formatted Excel file and push it to GitHub:
    ```bash
    python3 update_leads.py
    ```

## Files Added/Modified
- `admin-dashboard.html`: Added "Export to Excel" button and CSV generation logic.
- `update_leads.py`: Python script to convert JSON leads to a formatted Excel file and commit to Git.
- `leads.xlsx`: The generated Excel file (will be created after running the script).
