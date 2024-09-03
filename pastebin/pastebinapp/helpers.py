from datetime import datetime, timedelta

def get_expriration_time(paste_expiration):
    match paste_expiration:
            case 'NO':
                return datetime.now() + timedelta(days=36500) # 36500 days = 100 years
            case 'BU':
                return datetime.now() + timedelta(days=36500)
            case '10M':
                return datetime.now() + timedelta(minutes=10)
            case '1H':
                return datetime.now() + timedelta(hours=1)
            case '1D':
                return datetime.now() + timedelta(days=1)
            case '1W':
                return datetime.now() + timedelta(weeks=1)
            case '2W':
                return datetime.now() + timedelta(weeks=2)
            case '1M':
                return datetime.now() + timedelta(days=30)
            case '6M':
                return datetime.now() + timedelta(days=183)
            case '1Y':
                return datetime.now() + timedelta(days=366)
        
