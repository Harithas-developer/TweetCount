
from collections import Counter 

def UserData(a):
	val = 0
	data = []
	output = []
	output_dict = {}
	output_values = {}
	while val<a:
		#Reading the tweet count values from the User
		count = int(input("Enter the count of tweets to be done"))
		newVal=0

		while newVal<count:
			#Reading the input data from the User
			tweet = input("Enter the name of the user and Tweet details")
			data.append(tweet)
			newVal=newVal+1

		#splitting the input data into tweet and user names
		names = [pref_names.split()[0] for pref_names in data]
		times = Counter(names) 
		repeat = times.values()
		

		for element in set(repeat):
			#calculating the max key value pair 
			creating_Values = ([(key, value) for key, value in sorted(times.items()) if value == element])
			if len(creating_Values) > 1:
				for (key, value) in dupl: 
					output_dict[key] = value

			max_value = max(times.values())
			temp_max_result = [(key, value) for key, value in sorted(times.items()) if value == max_value] 
			

			if temp_max_result != creating_Values: 
				for (key,value) in temp_max_result: 
					output_dict[key] = value

		output.append(output_dict)					
		data = []
		output_dict={}
		val=val+1

	for values in output:
		for key, value in values.items():
			output_values[key]= value
	
	for key,value in output_values.items():
		print(key,value)


if __name__ == "__main__":
	#Reading the count values to cycle the input
    a = int(input("Please Enter the number of Counts"))
    UserData(a)
