from client import EvFleetSubscriptionBatteryHealthTelematicsClient

def main():
    client = EvFleetSubscriptionBatteryHealthTelematicsClient()
    res = client.assess_ev_subscription_asset('EV_POLESTAR2_04', 31000, 97.8)
    print('Assessment: ' + res['assessment_id'] + ' for ' + res['vehicle_id'])
    print('Subscription: $' + str(res['all_inclusive_monthly_subscription_usd']) + '/mo (All Inclusive: ' + str(res['insurance_charging_included']) + ')')
    print('Battery SOH: ' + str(res['battery_state_of_health_soh_pct']) + '% | Second-Life Residual: $' + str(res['second_life_bess_residual_value_usd']))

if __name__ == '__main__':
    main()
