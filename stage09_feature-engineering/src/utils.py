"""Utility functions for Stage 09: Feature Engineering."""

import pandas as pd
import numpy as np

def create_income_to_balance_ratio(df, income_col='income', balance_col='account_balance'):
    """Calculate income to balance ratio."""
    df['income_to_balance_ratio'] = df[income_col] / (df[balance_col] + 1)  # avoid division by zero
    return df

def create_transactions_per_year(df, transactions_col='num_transactions', tenure_col='tenure_years'):
    """Calculate transactions per year."""
    df['transactions_per_year'] = df[transactions_col] * 12 / (df[tenure_col] + 1)  # avoid division by zero
    return df

def flag_recent_activity(df, last_login_col='last_login_days_ago', days_threshold=30):
    """Flag active users based on last login threshold."""
    df['is_active'] = (df[last_login_col] <= days_threshold).astype(int)
    return df
