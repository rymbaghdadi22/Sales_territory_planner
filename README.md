Sales Territory Planner
Overview
The Sales Territory Planner is an Odoo 17 module designed to optimize and manage sales routes for Global Distributors, a company specializing in supplying products to retail stores. This module addresses key challenges in sales route planning, customer visit tracking, inventory monitoring at customer locations, and provides a comprehensive dashboard for sales managers.
Problem Definition
Sales managers face several challenges that this module aims to solve:
Sales Route Planning: The module allows managers to assign regions and create specific routes for sales representatives, ensuring efficient coverage of target areas without conflicts or overlap.
Customer Visits: The system tracks regular visits by sales representatives to both potential and existing customers, ensuring they meet defined schedules.
Stock Monitoring at Customer Locations: The module tracks inventory of products located at customer sites, helping with timely restocking services.
Dashboard for Monitoring and Reporting: A central dashboard enables sales managers to monitor active routes, view sales performance, and ensure adequate coverage of all areas.
Features
Sales Route Planning and Assignment
Route Creation: Sales managers can create routes and define regions, specifying coverage areas and planned visit schedules.
Route Assignment: Routes can be assigned to specific sales representatives, ensuring no overlap in coverage.
Route Modification: Managers can modify routes as needed without impacting existing data.
Customer Visit Scheduling and Tracking
Visit Scheduling: Sales representatives can log upcoming visits and their objectives.
Visit Check-ins: Check-in functionality allows sales representatives to confirm visits when they arrive on-site.
Visit Reporting: Sales representatives can report on visit outcomes, including customer feedback, inventory levels, and sales discussions.
Inventory Monitoring at Customer Locations
Inventory Entry: Sales representatives can enter inventory levels at each customer location.
Stock Alerts: The system notifies sales representatives and managers when inventory levels fall below a certain threshold.
Sales Metrics: The module tracks sales and inventory turnover for each product at customer locations.
Sales Dashboard for Real-Time Monitoring
Route Overview: Visualizes each sales representative's assigned routes and coverage areas, with alerts for unvisited customers.
Visit Summary: Displays a summary of recent visits, including outcomes, customer feedback, and inventory status.
Inventory Status: Shows inventory levels across customer locations, highlighting areas needing immediate restocking.

Development Challenges and Solutions
Challenge 1: JavaScript Integration with Odoo QWeb Templates
When developing the sales dashboard, I encountered difficulties integrating JavaScript charts and visualizations with Odoo's QWeb templating system. The dashboard components weren't rendering properly, and there were conflicts between the JavaScript libraries and Odoo's asset bundling system.
I resolved this by:
Creating a separate JavaScript asset bundle specifically for the dashboard
Using Odoo's widget system to properly initialize chart components after the DOM was fully loaded
Implementing proper event delegation to ensure dashboard elements responded correctly to user interactions
Using Odoo's built-in translation system to ensure all dashboard labels were properly localized
Challenge 2: While defining models for sales regions, routes, and customer visits, I encountered access issues during testing. Some users couldn’t access or modify the records as expected, and I didn’t initially understand why.
Resolution:
Learned how to define and apply security access control files (ir.model.access.csv)
Configured record rules to allow only assigned salespeople to view and manage their data

Tested with different user roles to validate proper access segregation

Dashboard Overview
The dashboard provides a comprehensive view of sales territories, customer visits, and inventory levels.
Territory Planning
Territory Map
The territory planning interface allows sales managers to define regions and assign them to sales representatives.
Customer Visit Tracking
Visit Tracking
The visit tracking interface enables sales representatives to log and report on customer visits.
Inventory Monitoring
The inventory monitoring interface shows stock levels at customer locations and highlights items needing restocking.
Future Enhancements
Route optimization based on proximity and visit priority
Integration with mapping services for visual route planning

Contributors
Rym Baghdadi
