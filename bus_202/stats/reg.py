def reg(df, y, x, fe=None, logistic=False):
    import statsmodels.api as sm
    import pandas as pd
    import numpy as np
    
    # Convert ivs to list if it's a single string
    if isinstance(x, str):
        x = [x]
    
    # Create copy of dataframe to avoid modifying original
    df_reg = df.copy()
    
    # Handle fixed effects if specified
    if fe is not None:
        # Convert fe to list if it's a single string
        if isinstance(fe, str):
            fe = [fe]
        
        # Create dummies for each fixed effect variable
        for fe_var in fe:
            # Create dummies, drop first category to avoid multicollinearity
            dummies = pd.get_dummies(df_reg[fe_var], prefix=fe_var, drop_first=True)
            
            # Add dummies to dataframe
            df_reg = pd.concat([df_reg, dummies], axis=1)
            
            # Add dummy column names to x list
            x.extend(dummies.columns)
    
    # Convert all variables to numeric, handling errors
    for col in [y] + x:
        try:
            df_reg[col] = pd.to_numeric(df_reg[col], errors='coerce')
        except Exception as e:
            print(f"Error converting {col} to numeric: {e}")
    
    # Drop rows with NaN values
    df_reg = df_reg.dropna(subset=[y] + x)
    
    # Create X and y, adding constant
    X = sm.add_constant(df_reg[x])
    y_data = df_reg[y]
    
    # Check for empty data after cleaning
    if len(X) == 0 or len(y_data) == 0:
        print("No data remaining after cleaning")
        return
    
    # Run appropriate regression
    if logistic:
        # Logistic regression
        model = sm.Logit(y_data, X)
    else:
        # OLS regression
        model = sm.OLS(y_data, X)
    
    # Fit model and return results
    try:
        results = model.fit()
        print(results.summary())
        return results  # Return the results object for further analysis if needed
    except Exception as e:
        print(f"Error fitting model: {e}")
        print("Data types in X:")
        print(X.dtypes)
        print("\nData type of y:")
        print(y_data.dtype)
