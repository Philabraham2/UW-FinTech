{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 223,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a python script for analyzing the financial records of our company\n",
    "\n",
    "# import pandas to help run script\n",
    "\n",
    "import pandas as pd\n",
    "from pathlib import Path\n",
    "import numpy as np\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Python Script needs to include the following:\n",
    "\n",
    "# The total number of months included in the dataset\n",
    "# The net total amount of Profit/losses over the entire period\n",
    "# The average of the changes in Profit/Losses over the entire period\n",
    "# The greatest increase in profits (date and amount) over the entire period\n",
    "# The greatest decrease in losses (date and amount) over the entire period\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 225,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jan-2010</td>\n",
       "      <td>867884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Feb-2010</td>\n",
       "      <td>984655</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mar-2010</td>\n",
       "      <td>322013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apr-2010</td>\n",
       "      <td>-69417</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May-2010</td>\n",
       "      <td>310503</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Date  Profit/Losses\n",
       "0  Jan-2010         867884\n",
       "1  Feb-2010         984655\n",
       "2  Mar-2010         322013\n",
       "3  Apr-2010         -69417\n",
       "4  May-2010         310503"
      ]
     },
     "execution_count": 225,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# create a file to the path \n",
    "csvpath = Path(\"../PyBank/raw_budget_data.csv\")\n",
    "\n",
    "# Time to read the CSV as a dataframe using Pandas\n",
    "\n",
    "budget_data = pd.read_csv(csvpath)\n",
    "budget_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 226,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Date             86\n",
       "Profit/Losses    86\n",
       "dtype: int64"
      ]
     },
     "execution_count": 226,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Quick check to see how many rows there are:\n",
    "budget_data.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "86\n"
     ]
    }
   ],
   "source": [
    "#Count the number of rows which will tell us the total amount of months:\n",
    "months = len(budget_data)\n",
    "print(months)\n",
    "\n",
    "#Creating a variable that will serve as a function to answer question 1:\n",
    "total_months = (f\"The total number of months in the data set is: {months} months\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 228,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "38382578\n"
     ]
    }
   ],
   "source": [
    "# The net total amount of Profit/losses over the entire period:\n",
    "\n",
    "#This function will help me add the total profit and losses found in the Profit/Losses column:\n",
    "totals = budget_data.sum(1)\n",
    "total_profit = sum(totals)\n",
    "print(total_profit)\n",
    "\n",
    "#Creating a variable that will serve as a function to answer question 2:\n",
    "total_profits = (f\"The total net amount of profit is: ${total_profit}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 229,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "      <th>Average Change</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jan-2010</td>\n",
       "      <td>867884</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Feb-2010</td>\n",
       "      <td>984655</td>\n",
       "      <td>116771.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mar-2010</td>\n",
       "      <td>322013</td>\n",
       "      <td>-662642.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apr-2010</td>\n",
       "      <td>-69417</td>\n",
       "      <td>-391430.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May-2010</td>\n",
       "      <td>310503</td>\n",
       "      <td>379920.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Date  Profit/Losses  Average Change\n",
       "0  Jan-2010         867884             NaN\n",
       "1  Feb-2010         984655        116771.0\n",
       "2  Mar-2010         322013       -662642.0\n",
       "3  Apr-2010         -69417       -391430.0\n",
       "4  May-2010         310503        379920.0"
      ]
     },
     "execution_count": 229,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# The average of the changes in Profit/Losses over the entire period:\n",
    "\n",
    "#First find the Average Change by creating a new column that determines the actual monthly changes:\n",
    "\n",
    "budget_data[\"Average Change\"] = budget_data[\"Profit/Losses\"] - budget_data[\"Profit/Losses\"].shift(1) \n",
    "budget_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 230,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-2315.12\n"
     ]
    }
   ],
   "source": [
    "#Now its time to determine the average change in the column Average Change:\n",
    "\n",
    "#First drop any missing datapoints as that will mess up the data:\n",
    "budget_data[\"Average Change\"] = budget_data[\"Average Change\"].dropna()\n",
    "\n",
    "#Now that its clean use the mean function here to determine the average of the Average changes in income. I am using the round function to round it to 2 places:\n",
    "average_budget_data = round(budget_data[\"Average Change\"].mean(), 2)\n",
    "print(average_budget_data)\n",
    "\n",
    "#Creating a variable that will serve as a function to answer question 3:\n",
    "average_budget_data_change = (f\"The average of the average change in profit/losses is: ${average_budget_data}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 231,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1926159.0\n",
      "25    Feb-2012\n",
      "Name: Date, dtype: object\n"
     ]
    }
   ],
   "source": [
    "# The greatest increase in profits (date and amount) over the entire period:\n",
    "\n",
    "#This function will allow me to locate which row has the greatest increase in profit:\n",
    "greatest_increase_profit = budget_data['Average Change'].max()\n",
    "print(greatest_increase_profit)\n",
    "\n",
    "#This will allow me to see what the date of the greatest increase in profit was: \n",
    "print(budget_data.loc[budget_data['Average Change']== 1926159]['Date'])\n",
    "\n",
    "#Using the printed .loc I am creating a function that uses the index value to help with creating a single output for the function allowing me to add it to the answer in a clean method:\n",
    "profit_gain_date =(budget_data.iloc[25,0])\n",
    "      \n",
    "# Creating a sentence using the data:\n",
    "greatest_increased_profit = (f\"Greatest increase in profits occurred on: {profit_gain_date} for ${greatest_increase_profit}\") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-2196167.0\n",
      "44    Sep-2013\n",
      "Name: Date, dtype: object\n"
     ]
    }
   ],
   "source": [
    "# The greatest decrease in losses (date and amount) over the entire period:\n",
    "\n",
    "#This function will allow me to locate which row has the greatest decrease in profit:\n",
    "greatest_decrease_profit = budget_data['Average Change'].min()\n",
    "print(greatest_decrease_profit)\n",
    "\n",
    "#This will allow me to see what the date of the greatest decrease in profit was:\n",
    "print(budget_data.loc[budget_data['Average Change']== -2196167]['Date'])\n",
    "\n",
    "#Using the printed .loc I am creating a function that uses the index value to help with creating a single output for the function allowing me to add it to the answer in a clean method:\n",
    "profit_loss_date =(budget_data.iloc[44,0])\n",
    "\n",
    "# Creating a sentence using the data:\n",
    "greatest_decreased_profit = (f\"Greatest decrease in profits occurred on: {profit_loss_date} for ${greatest_decrease_profit}\")  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 233,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-----------------------------------------------------------------------------------------------------------------\n",
      "The data presented above this line were used for sanity checks please refer to the bottom data for final results\n"
     ]
    }
   ],
   "source": [
    "print(\"-----------------------------------------------------------------------------------------------------------------\")\n",
    "print(f\"The data presented above this line were used for sanity checks please refer to the bottom data for final results\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 234,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis:\n",
      "\n",
      "The total number of months in the data set is: 86 months\n",
      "The total net amount of profit is: $38382578\n",
      "The average of the average change in profit/losses is: $-2315.12\n",
      "Greatest increase in profits occurred on: Feb-2012 for $1926159.0\n",
      "Greatest decrease in profits occurred on: Sep-2013 for $-2196167.0\n"
     ]
    }
   ],
   "source": [
    "# Time to print the results\n",
    "\n",
    "print(f\"Financial Analysis:\")\n",
    "print()\n",
    "print(total_months)\n",
    "print(total_profits)\n",
    "print(average_budget_data_change)\n",
    "print(greatest_increased_profit)\n",
    "print(greatest_decreased_profit)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
