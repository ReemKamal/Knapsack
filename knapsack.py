#import quickSort
import pandas as pd
import numpy as np


def partition(arr0, arr1 , arr2 ,  low, high):
	i = (low-1)		 
	pivot0 = arr0[high]
	
	for j in range(low, high):
		if arr0[j] <= pivot0:
			i = i+1
			arr0[i], arr0[j] = arr0[j], arr0[i]
			arr1[i], arr1[j] = arr1[j], arr1[i]
			arr2[i], arr2[j] = arr2[j], arr2[i]

	arr0[i+1], arr0[high] = arr0[high], arr0[i+1]
	arr1[i+1], arr1[high] = arr1[high], arr1[i+1]
	arr2[i+1], arr2[high] = arr2[high], arr2[i+1]
	return (i+1)

def quickSort(arr0 , arr1 , arr2 , low, high):
	if len(arr0) == 1:
		return arr0
	if low < high:
		pi = partition(arr0, arr1 , arr2, low, high)
		quickSort(arr0, arr1 , arr2 ,  low, pi-1)
		quickSort(arr0, arr1 , arr2 ,  pi+1, high)
	df = pd.DataFrame(  list(zip(arr0 , arr1 , arr2)) , columns=["A" , "B" , "C"] )
	return df



def insert_method():
	print("Choose how do you want to input your data:")
	print("1. Enter your data Manually.")
	print("2. Using the default Excel file sheet.")
	print("3. Using the default CSV file.")
	print("4. Using the default XML file.")
	print("5. Using the default JSON file.")

	method = int(input())

	# 1.  using sheet // Manually
	'''
	impport the sheet
	read the sheet into 2 lists profit[] weight[]    
	'''
	if method == 1: #manual
		print('Please enter the profit values sepatated by space') 
		profit_array = np.asarray(list(map(int, input().split(" "))))
		print('Please enter the weight values sepatated by space')
		weight_array = np.asarray(list(map(int, input().split(" "))))
		p_w_array = np.divide(profit_array, weight_array)

		print(f'Profit: {profit_array}	Weights: {weight_array}	p/w: {p_w_array}')

		#create a dictionery of arrays to usee it's keys to know which feature we will sort on in the quick sort
		# Creating an empty dictionary
		data_dict = {}
		data_dict["1"] = profit_array
		data_dict["2"] = weight_array
		data_dict["3"] = p_w_array
		return data_dict


	else:
		if method == 2:
			#read the data
			data_df = pd.read_excel('myData.xlsx', 'Sheet1')
		elif method == 3:
			#read data
			data_df = pd.read_csv('myData.csv')
		elif method == 4:
			#read data
			data_df = pd.read_xml('myData.xml')
		elif method == 5:
			#read data
			data_df = pd.read_json('myData.json')

		#calc the p/w and add to df
		data_df["p/w"] = data_df["Profit"]/data_df["Weight"]
		#convert cols to np arrays
		profit_col = data_df["Profit"].to_numpy()
		weight_col = data_df["Weight"].to_numpy()
		p_w_col = data_df["p/w"].to_numpy()
		#add arrays to the dictionery
		data_dict = {}
		data_dict["1"] = profit_col
		data_dict["2"] = weight_col
		data_dict["3"] = p_w_col
		#return the dictionery
		return data_dict

		



def operations(data_dict):
	#3. choose the feture  to arrange on 
	print("(1) as Profit  (2) as Weight  (3) as profit/weight ")
	print("Please enter the the 3 numbers considering the fist number as the feature to sort on ")
	#sorted_df = quickSort(data_dict[input()] , data_dict[input()] , data_dict[input()] , 0 , len(data_dict["1"])-1 )
	keyA = input()
	keyB = input()
	keyC = input()
	sorted_df = quickSort(data_dict[keyA] , data_dict[keyB] , data_dict[keyC] , 0 , len(data_dict["1"])-1)
	#edit the original data_dict we have and return it out of the function
	data_dict[keyA] = sorted_df["A"].to_numpy()
	data_dict[keyB] = sorted_df["B"].to_numpy()
	data_dict[keyC] = sorted_df["C"].to_numpy()
	return data_dict



def strategy(strategy_flag):
	# strategies will have the same code until we are choosing 
	#  the last element we will use the flag then 
	#  KNAPSACK CODE...

	#in case  0/1 Knapsack
	#reconvert the df to arrays
	profit = sorted_dict["1"]
	weight = sorted_dict["2"]
	p_w = sorted_dict["3"]

	totalProf = 0
	totalWeight = 0
	for i in reversed(range(len(profit))):
		if totalWeight + weight[i] <= sack:
			totalProf = totalProf + profit[i]
			totalWeight = totalWeight + weight[i]
			#print("Total Weight now ",totalWeight)
			#print("Total Profit now ",totalProf)

		elif strategy_flag == 1 :  #fractional
			totalProf = totalProf + p_w[i]*(sack-totalWeight)
			totalWeight = totalWeight + sack-totalWeight
			#print("Total Weight now ",totalWeight)
			#print("Total Profit now ",totalProf)
			break

		else:
			continue        

	return totalProf








print("Knapsack Program")
program_falg = 1

while(program_falg == 1):
	program_falg = 0
	data_dict = insert_method()

	#2. Enter your sack size
	print("Please Enter the sack size:")
	sack = int(input())
	

	program_falg2 = 1
	while(program_falg2 == 1):
		program_falg2 = 0
		#3. cheoose what to arrange on and arrange
		sorted_dict  = operations(data_dict)
		#print(sorted_dict)
		#4. 0 => Fractional Knapsack   1 => 0/1 Knapsack 
		print("Enter the Profit calculation method:")
		print("1. Fractional Knapsack")
		print("2. 0/1 Knapsack")

		strategy_flag = int(input())
		total_prof = strategy(strategy_flag)
		print(f'The Total profit will be {total_prof}')

		print("Do you want to try anohter strategy of calculating? y/n")
		again = input()
		if again == "y":
			program_falg2 = 1
		else:
			break

	print("Do you want to try anohter dataset? y/n")
	again = input()
	if again == "y":
			program_falg = 1
	else:
		print("THANK YOU FOR USING KNAPSACK CALCULATOR !")
		break