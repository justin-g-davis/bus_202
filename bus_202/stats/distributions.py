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

def t_ppf(p, n):
    """Returns t-value for a given probability and sample size"""
    import math
    if not 0.001 <= p <= 0.999:
        raise ValueError("Probability must be between 0.001 and 0.999")
    if n < 2:
        raise ValueError("Sample size must be at least 2")
    
    if p < 0.5:
        return -t_ppf(1 - p, n)
    
    df = n - 1
    z = z_ppf(p)
    
    g1 = (z**3 + z) / (4 * df)
    g2 = (5*z**5 + 16*z**3 + 3*z) / (96 * df**2)
    g3 = (3*z**7 + 19*z**5 + 17*z**3 - 15*z) / (384 * df**3)
    
    return z + g1 + g2 + g3

def t_cdf(t, n):
    """Returns probability for a given t-value and sample size"""
    import math
    if n < 2:
        raise ValueError("Sample size must be at least 2")
    
    if t < 0:
        return 1 - t_cdf(-t, n)
    
    df = n - 1
    # Convert t to z
    z = t * math.sqrt((df-2)/df) * (1 + t*t/(2*df))**(-0.5)
    return z_cdf(z)
