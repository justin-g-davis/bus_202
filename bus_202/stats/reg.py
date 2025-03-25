def reg(df, y, x, fe=None, logistic=False):
    import statsmodels.api as sm
    import pandas as pd
    import numpy as np
    
    # Convert ivs to list if it's a single string
    if isinstance(x, str):
        x = [x]
    
    # Create copy of dataframe to avoid modifying original
    df_reg = df.copy()
    
    # Convert main variables to numeric
    numeric_cols = [y] + x
    for col in numeric_cols:
        df_reg[col] = pd.to_numeric(df_reg[col], errors='coerce')
    
    # Handle fixed effects if specified
    if fe is not None:
        # Convert fe to list if it's a single string
        if isinstance(fe, str):
            fe = [fe]
        
        # Create dummies for each fixed effect variable
        dummy_cols = []
        for fe_var in fe:
            # Create dummies, drop first category to avoid multicollinearity
            dummies = pd.get_dummies(df_reg[fe_var], prefix=fe_var, drop_first=True, dtype=float)
            
            # Store dummy column names
            dummy_cols.extend(dummies.columns)
            
            # Add dummies to dataframe
            df_reg = pd.concat([df_reg, dummies], axis=1)
    
        # Add dummy columns to x list
        x = x + dummy_cols
    
    # Drop rows with NaN values
    df_reg = df_reg.dropna(subset=[y] + x)
    
    # Create X and y, adding constant
    X = sm.add_constant(df_reg[x].astype(float))
    y_data = df_reg[y].astype(float)
    
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
        print("\nData types in X:")
        print(X.dtypes)
        print("\nData type of y:")
        print(y_data.dtype)
        print("\nShape of X:", X.shape)
        print("Shape of y:", y_data.shape)
