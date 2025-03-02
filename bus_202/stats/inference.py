from .distributions import z_ppf, t_ppf

def ci(sample_stat, n, confidence_level=0.95, is_proportion=False, std=None):
    """
    Calculates confidence interval for a mean or proportion
    
    Parameters:
    sample_stat: Sample statistic (mean or proportion)
    n: Sample size
    confidence_level: Usually 0.95 for 95% confidence
    is_proportion: True if working with proportions
    std: Sample standard deviation (needed for means)
    """
    if not 0 < confidence_level < 1:
        raise ValueError("Confidence level must be between 0 and 1")
    
    alpha = 1 - confidence_level
    p = 1 - alpha/2
    
    if is_proportion:
        if not 0 <= sample_stat <= 1:
            raise ValueError("Proportion must be between 0 and 1")
        
        z = z_ppf(p)
        se = math.sqrt((sample_stat * (1 - sample_stat)) / n)
        margin = z * se
        
    else:
        if std is None:
            raise ValueError("Standard deviation required for means")
            
        df = n - 1
        t = t_ppf(p, df)
        se = std / math.sqrt(n)
        margin = t * se
    
    return (round(sample_stat - margin, 3), round(sample_stat + margin, 3))
