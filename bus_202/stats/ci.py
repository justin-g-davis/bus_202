def ci(stat, n, std=None , is_proportion=False, cl=0.95):
    """Returns confidence interval for a mean or proportion"""
    from scipy import stats
    if not 0 < confidence_level < 1:
        raise ValueError("Confidence level must be between 0 and 1")
    
    alpha = 1 - confidence_level
    p = 1 - alpha/2
    
    if is_proportion:
        if not 0 <= stat <= 1:
            raise ValueError("Proportion must be between 0 and 1")
        
        se = math.sqrt((stat * (1 - stat)) / n)
        margin = stats.norm.ppf(p) * se
        
    else:
        if std is None:
            raise ValueError("Standard deviation required for means")
            
        df = n - 1
        se = std / math.sqrt(n)
        margin = stats.t.ppf(p, df) * se
    
    return (round(stat - margin, 3), round(stat + margin, 3))
