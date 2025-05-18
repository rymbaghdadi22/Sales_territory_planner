/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, useState, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

class SalesTerritoryDashboard extends Component {
    setup() {
        this.state = useState({
            territories: [],
            visits: [],
            inventory: [],
            loading: true,
        });
        
        this.orm = useService("orm");
        this.actionService = useService("action");
        
        onWillStart(async () => {
            await this.fetchDashboardData();
        });
    }
    
    async fetchDashboardData() {
        try {
            const [territories, visits, inventory] = await Promise.all([
                this.fetchTerritories(),
                this.fetchRecentVisits(),
                this.fetchInventoryStatus()
            ]);
            
            this.state.territories = territories;
            this.state.visits = visits;
            this.state.inventory = inventory;
            this.state.loading = false;
        } catch (error) {
            console.error("Error fetching dashboard data:", error);
        }
    }
    
    async fetchTerritories() {
        return this.orm.searchRead(
            "sales.territory",
            [],
            ["name", "sales_person_id", "zone", "visit_day"]
        );
    }
    
    async fetchRecentVisits() {
        const thirtyDaysAgo = new Date();
        thirtyDaysAgo.setDate(thirtyDaysAgo.getDate() - 30);
        const dateString = thirtyDaysAgo.toISOString().split('T')[0]; 
        
        return this.orm.searchRead(
            "sales.customer.visit",
            [["visit_date", ">=", dateString]],
            ["name", "customer_id", "visit_date", "check_in_time", "feedback", "inventory_status", "sales_person_id"],
            { order: "visit_date desc", limit: 10 }
        );
    }
    
    async fetchInventoryStatus() {
        return this.orm.searchRead(
            "customer.inventory",
            [],
            ["customer_id", "product_id", "current_stock", "min_stock_level", "visit_id", "last_updated"],
            { order: "last_updated desc" }
        );
    }
    
    openTerritory(territoryId) {
        this.actionService.doAction({
            type: "ir.actions.act_window",
            res_model: "sales.territory",
            res_id: territoryId,
            views: [[false, "form"]],
            target: "current",
        });
    }
    
    openVisit(visitId) {
        this.actionService.doAction({
            type: "ir.actions.act_window",
            res_model: "sales.customer.visit",
            res_id: visitId,
            views: [[false, "form"]],
            target: "current",
        });
    }
    
    openInventory(inventoryId) {
        this.actionService.doAction({
            type: "ir.actions.act_window",
            res_model: "customer.inventory",
            res_id: inventoryId,
            views: [[false, "form"]],
            target: "current",
        });
    }
}

SalesTerritoryDashboard.template = "sales_territory_planner.Dashboard";
registry.category("actions").add("sales_territory_dashboard_tag", SalesTerritoryDashboard);

export default SalesTerritoryDashboard;
