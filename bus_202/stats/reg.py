def reg(df, y, x, fe=None, logistic=False, show_fe=False):
    import statsmodels.api as sm
    import pandas as pd
    import numpy as np
    
    # Convert ivs to list if it's a single string
    if isinstance(x, str):
        x = [x]
    
    # Store original x variables before adding dummies
    original_x = ['const'] + x.copy()
    
    # Create copy of dataframe to avoid modifying original
    df_reg = df.copy()
    
    # Convert main variables to numeric
    numeric_cols = [y] + x
    for col in numeric_cols:
        df_reg[col] = pd.to_numeric(df_reg[col], errors='coerce')
    
    # Handle fixed effects if specified
    dummy_cols = []
    if fe is not None:
        # Convert fe to list if it's a single string
        if isinstance(fe, str):
            fe = [fe]
        
        # Create dummies for each fixed effect variable
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
        model = sm.Logit(y_data, X)
    else:
        model = sm.OLS(y_data, X)
    
    # Fit model and return results
    try:
        results = model.fit()
        
        # Create custom summary if hiding fixed effects
        if not show_fe:
            # Get summary as DataFrame
            summary_df = pd.read_html(results.summary().tables[1].as_html(), header=0)[0]
            
            # Filter for only original variables
            summary_df = summary_df[summary_df.index.isin(original_x)]
            
            # Print modified summary
            print("OLS Regression Results")
            print("=" * 80)
            print(f"Dep. Variable: {y}")
            print(f"R-squared: {results.rsquared:.4f}")
            print(f"Adj. R-squared: {results.rsquared_adj:.4f}")
            print(f"No. Observations: {results.nobs}")
            print("=" * 80)
            print(summary_df.to_string())
            print("=" * 80)
            
            # Add note about fixed effects
            if fe:
                fe_str = ', '.join(fe) if isinstance(fe, list) else fe
                print(f"\nNote: Fixed effects for {fe_str} included but not shown")
                print(f"Number of fixed effects: {len(dummy_cols)}")
        else:
            print(results.summary())
            
        return results
    
    except Exception as e:
        print(f"Error fitting model: {e}")
        print("\nData types in X:")
        print(X.dtypes)
        print("\nData type of y:")
        print(y_data.dtype)
        print("\nShape of X:", X.shape)
        print("Shape of y:", y_data.shape)
