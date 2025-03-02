def ci(sample_mean, n, confidence_level=0.95, is_proportion=False, std=None):
    """Returns confidence interval for a mean or proportion"""
    from scipy import stats
    if not 0 < confidence_level < 1:
        raise ValueError("Confidence level must be between 0 and 1")
    
    alpha = 1 - confidence_level
    p = 1 - alpha/2
    
    if is_proportion:
        if not 0 <= sample_stat <= 1:
            raise ValueError("Proportion must be between 0 and 1")
        
        se = math.sqrt((sample_stat * (1 - sample_stat)) / n)
        margin = stats.norm.ppf(p) * se
        
    else:
        if std is None:
            raise ValueError("Standard deviation required for means")
            
        df = n - 1
        se = std / math.sqrt(n)
        margin = stats.t.ppf(p, df) * se
    
    return (round(sample_stat - margin, 3), round(sample_stat + margin, 3))
