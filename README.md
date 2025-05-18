What It Is: 

The Sales Territory Planner is a custom-built Odoo 17 module created for Global Distributors to streamline sales route planning, customer visit tracking, and on-site inventory monitoring. It helps sales managers stay in control with a real-time dashboard that makes data actionable.

What Problem Does It Solve?

Sales teams often struggle with:
Overlapping routes and inefficient territory coverage
Missed or untracked customer visits
No visibility into inventory levels at customer locations
Lack of centralized, up-to-date performance data
This module fixes all that with automation, structure, and clear reporting.

Core Features:

1.Smart Route Planning
Create sales regions and define detailed routes
Assign routes to specific reps to avoid overlaps
Modify routes anytime without losing data

2.Customer Visit Management
Schedule and log upcoming visits
Reps can check in on-site and record visit outcomes
Collect feedback, discuss sales, and update stock info on the go

3.Inventory Monitoring at Customer Sites
Track product stock levels at customer locations
Get low-stock alerts to enable timely restocking
Monitor sales turnover per product at each site

4.Real-Time Sales Dashboard
Visual overview of sales reps’ routes and coverage
See summaries of recent visits, feedback, and stock updates
Quickly spot unvisited customers or urgent inventory needs

Development Hurdles & How I Solved Them:
1.Challenge 1: JavaScript + Odoo QWeb Compatibility
Problem: JS charts wouldn’t render correctly in Odoo’s templating system

Solution:
Built a dedicated JS asset bundle for the dashboard
Used Odoo’s widget system for proper chart initialization
Managed events with delegation for responsive elements
Enabled translations for multilingual dashboard labels

2.Challenge 2: Access Control in Custom Models
Problem: Sales reps couldn't access or edit their assigned data

Solution:
Learned and applied ir.model.access.csv files
Set up record rules to restrict visibility by user role
Tested access with various user types to ensure security

What’s Next?(for later modifications and improvements )
Smart route optimization (based on location & priority)
Map integration for visual route planning

Contributor
Rym Baghdadi.










