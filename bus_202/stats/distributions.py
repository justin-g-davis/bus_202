def z_ppf(p):
    """Returns z-score for a given probability"""
    import math
    if not 0.001 <= p <= 0.999:
        raise ValueError("Probability must be between 0.001 and 0.999")
    
    # Fix: For p > 0.5, we want positive z-score
    negative = p < 0.5
    if negative:
        p = 1 - p
    
    c0, c1, c2 = 2.515517, 0.802853, 0.010328
    d1, d2, d3 = 1.432788, 0.189269, 0.001308
    
    t = math.sqrt(-2 * math.log(p))
    z = t - (c0 + c1*t + c2*t**2) / (1 + d1*t + d2*t**2 + d3*t**3)
    
    return -z if negative else z

def z_cdf(z):
    """Returns probability for a given z-score"""
    import math
    if z < 0:
        return 1 - z_cdf(-z)
    
    b0 = 0.2316419
    b1, b2 = 0.319381530, -0.356563782
    b3, b4 = 1.781477937, -1.821255978
    b5 = 1.330274429
    
    t = 1 / (1 + b0 * z)
    poly = b1*t + b2*t**2 + b3*t**3 + b4*t**4 + b5*t**5
    
    pdf = math.exp(-z*z/2) / math.sqrt(2*math.pi)
    return round(1 - pdf * poly, 6)

def t_ppf(p, df):
    """Returns t-value for a given probability and degrees of freedom"""
    import math
    if not 0.001 <= p <= 0.999:
        raise ValueError("Probability must be between 0.001 and 0.999")
    if df < 1:
        raise ValueError("Degrees of freedom must be positive")
    
    z = z_ppf(p)
    if df <= 2:
        return z
    
    g1 = (z**3 + z) / 4
    g2 = (5*z**5 + 16*z**3 + 3*z) / 96
    
    return round(z + g1/df + g2/(df**2), 6)

def t_cdf(t, df):
    """Returns probability for a given t-value and degrees of freedom"""
    import math
    if df < 1:
        raise ValueError("Degrees of freedom must be positive")
    
    if t < 0:
        return 1 - t_cdf(-t, df)
    
    if df <= 2:
        return z_cdf(t)
    
    z = t - (t**3 + t)/(4*df) - (5*t**5 + 16*t**3 + 3*t)/(96*df**2)
    
    return round(z_cdf(z), 6)
