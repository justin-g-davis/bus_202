def z_ppf(p):
    """Returns z-score for a given probability"""
    import math
    if not 0.001 <= p <= 0.999:
        raise ValueError("Probability must be between 0.001 and 0.999")
    
    if p < 0.5:
        return -z_ppf(1 - p)
    
    t = math.sqrt(-2 * math.log(1 - p))
    c0, c1, c2 = 2.515517, 0.802853, 0.010328
    d1, d2, d3 = 1.432788, 0.189269, 0.001308
    
    z = t - (c0 + c1*t + c2*t**2) / (1 + d1*t + d2*t**2 + d3*t**3)
    return z

def z_cdf(z):
    """Returns probability for a given z-score"""
    import math
    if z < 0:
        return 1 - z_cdf(-z)
    
    t = 1 / (1 + 0.2316419 * z)
    poly = 0.319381530 * t \
         - 0.356563782 * t**2 \
         + 1.781477937 * t**3 \
         - 1.821255978 * t**4 \
         + 1.330274429 * t**5
    
    return 1 - (math.exp(-z*z/2) / math.sqrt(2*math.pi)) * poly

def t_ppf(p, df):
    """Returns t-value for a given probability and degrees of freedom"""
    import math
    if not 0.001 <= p <= 0.999:
        raise ValueError("Probability must be between 0.001 and 0.999")
    if df < 1:
        raise ValueError("Degrees of freedom must be positive")
    
    if p < 0.5:
        return -t_ppf(1 - p, df)
    
    z = z_ppf(p)
    g1 = (z**3 + z) / 4
    g2 = (5*z**5 + 16*z**3 + 3*z) / 96
    
    return z + g1/df + g2/(df**2)

def t_cdf(t, df):
    """Returns probability for a given t-value and degrees of freedom"""
    import math
    if df < 1:
        raise ValueError("Degrees of freedom must be positive")
    
    if t < 0:
        return 1 - t_cdf(-t, df)
    
    z = t * (1 - 1/(4*df) - 7/(32*df**2) - 19/(128*df**3))
    return z_cdf(z)
