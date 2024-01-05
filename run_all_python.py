import itertools
import subprocess

# Iterate through the parameter combinations and execute the command   

#-----------------------------------------------------------
# Running Vsion 21, 49, 100
#-----------------------------------------------------------
        
data = {'Vision_21':{'n_groups':3,'n_students':21,'n_features':2},
		'Vision_49':{'n_groups':10,'n_students':49,'n_features':1},
		'Vision_100':{'n_groups':10,'n_students':100,'n_features':2},
		'Vision_200':{'n_groups':20,'n_students':200,'n_features':2},
        'Vision_300':{'n_groups':30,'n_students':300,'n_features':2},
        'Vision_400':{'n_groups':40,'n_students':400,'n_features':2}}

#data = {'Vision_100':{'n_groups':10,'n_students':100,'n_features':2},
#        'Vision_200':{'n_groups':20,'n_students':200,'n_features':2}}
  
for data_instance in data:

	#instance_data_folder = data_folder_path.joinpath(data_instance)

	alpha_file_name = f'{data_instance}_alpha.txt'
	#alpha_file_name = instance_data_folder.joinpath(alpha_bat)

	beta_file_name = f'{data_instance}_beta.txt'
	#beta_file_name = instance_data_folder.joinpath(beta_bat)

	theta_file_name = f'{data_instance}_theta.txt'
	#theta_file_name = instance_data_folder.joinpath(theta_bat)

	#x_file_name = f'{data_instance}_x_min_sum.txt'
	x_file_name = f'{data_instance}_x_min_max.txt'
	#x_file_name = instance_data_folder.joinpath(theta_bat)

	n_groups = data[data_instance]['n_groups']
	n_students = data[data_instance]['n_students']
	n_features = data[data_instance]['n_features']

	max_init = '2'
	taylor = '0'
	#problem = '0' #min-sum
	problem = '1' #min-max
	
	# CGFP_project.exe Vision_21_alpha.txt Vision_21_beta.txt Vision_21_theta.txt Vision_21_x_min_sum.txt 21 2 3 0 0 0 0 0 0 2 8 600 0.0
	
	for method in ['0','1']:
		for LB in ['0','1']:
			for UB in ['0','1']:
				for MW in ['0','1']:
					phrase = f'CGFP_project.exe {alpha_file_name} {beta_file_name} {theta_file_name} {x_file_name} {n_students} {n_features} {n_groups} {method} {problem} {taylor} {LB} {UB} {MW} {max_init} 8 600 0.0'
					print(phrase)
					subprocess.run(phrase, shell=True)
