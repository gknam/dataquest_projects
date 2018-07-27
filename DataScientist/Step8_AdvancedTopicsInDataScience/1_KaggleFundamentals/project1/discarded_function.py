# This function has been created by Kie Woo Nam

def remove_corr_features(X, train, holdout, fi_all, thres):
    """
    In X, when two features are correlated, remove the one with less importance
    """
    X_corr = X.corr()
    hi_corr_features = dict()
    removed_features = []
    for col1 in X_corr:
        corrs = X_corr[col1]
        
        # Get highly correlated features
        corrs_hi = corrs.drop(col1)[abs(corrs) > thres]
        for col2, corr_coef in corrs_hi.iteritems():

            # Do this only once per pair
            if (col2 + " and " + col1) not in hi_corr_features:
                
                # Identify less important feature
                cols = [col1, col2]
                fi_cols = fi_all[fi_all["Feature"].isin(cols)]
                fi_cols_ranks = fi_cols["Rank"]
                is_less_important = (fi_cols_ranks == fi_cols_ranks.min())
                col_less_important = fi_cols["Feature"][is_less_important].values[0]
                
                # Remove less important feature from dataframes
                X = X.drop(col_less_important, axis=1)
                train = train.drop(col_less_important, axis=1)
                holdout = holdout.drop(col_less_important, axis=1)
                fi_all = fi_all[~fi_all["Feature"].isin([col_less_important])]
                
                # Record less important feature
                hi_corr_features[col1 + " and " + col2] = {}
                hi_corr_features[col1 + " and " + col2]["Removed"] = col_less_important
                
                # Record correlation coefficient
                hi_corr_features[col1 + " and " + col2]["corr_coef"] = corr_coef
                
                removed_features.append(col_less_important)
                
    print("Highly correlated features (pearson's correlation coefficient > {}:".format(thres))
    pprint(hi_corr_features)
    print()
    
    print("Removed features:")
    pprint(removed_features)
                
    return X, train, holdout, fi_all