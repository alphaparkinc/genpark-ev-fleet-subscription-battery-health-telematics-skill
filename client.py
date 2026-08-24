class EvFleetSubscriptionBatteryHealthTelematicsClient:
    def assess_ev_subscription_asset(self, vehicle_id='EV_IONIQ5_8812', odometer_km=42000, current_soh_pct=96.4):
        return {
            'assessment_id': 'evr_sub_5519',
            'vehicle_id': vehicle_id,
            'all_inclusive_monthly_subscription_usd': 580.0,
            'battery_state_of_health_soh_pct': current_soh_pct,
            'second_life_bess_residual_value_usd': 4200.0,
            'telematics_predictive_maintenance_ok': True,
            'insurance_charging_included': True
        }
