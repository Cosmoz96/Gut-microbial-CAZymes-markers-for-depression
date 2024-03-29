import argparse
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, cross_val_predict, GridSearchCV

def read_arg():
    parser = argparse.ArgumentParser()
    parser.description = f'Training script with random forest model.'
    parser.add_argument('-i', '--input', required=True, help='Data frame for model training, csv format.')
    args = parser.parse_args()
    print(parser.description)
    return args

def training(file):
	# load data
	train = pd.read_csv(file)
	x_train = train[["AA10",
			"AA9",
			"AA2",
			"AA3",
			"AA3_2",
			"AA4",
			"AA6",
			"AA7",
			"CBM11",
			"CBM12",
			"CBM13",
			"CBM14",
			"CBM15",
			"CBM16",
			"CBM17",
			"CBM18",
			"CBM64",
			"CBM2",
			"CBM20",
			"CBM21",
			"CBM22",
			"CBM60",
			"CBM23",
			"CBM25",
			"CBM26",
			"CBM27",
			"CBM19",
			"CBM28",
			"CBM3",
			"CBM59",
			"CBM30",
			"CBM32",
			"CBM34",
			"CBM35",
			"CBM36",
			"CBM24",
			"CBM37",
			"CBM38",
			"CBM4",
			"CBM40",
			"CBM41",
			"CBM39",
			"CBM81",
			"CBM42",
			"CBM44",
			"CBM45",
			"CBM46",
			"CBM47",
			"CBM48",
			"CBM49",
			"CBM5",
			"CBM50",
			"CBM51",
			"CBM53",
			"CBM54",
			"CBM29",
			"CBM1",
			"CBM80",
			"CBM56",
			"GH43_24",
			"CBM58",
			"CBM6",
			"CBM61",
			"CBM62",
			"CBM63",
			"CBM65",
			"CBM66",
			"CBM67",
			"CBM68",
			"CBM69",
			"CBM70",
			"CBM71",
			"CBM72",
			"CBM73",
			"CBM74",
			"CBM75",
			"CBM76",
			"CBM77",
			"CBM78",
			"CBM31",
			"CBM79",
			"CBM8",
			"CBM9",
			"CE1",
			"CE10",
			"CE11",
			"CE12",
			"CE13",
			"CE14",
			"CE15",
			"CE2",
			"CE3",
			"CE4",
			"CE5",
			"CE6",
			"CE7",
			"CE8",
			"CE9",
			"GH1",
			"GH10",
			"GH43_4",
			"GH102",
			"GH103",
			"GH104",
			"GH105",
			"GH20",
			"GH108",
			"GH109",
			"GH11",
			"GH110",
			"GH111",
			"GH112",
			"GH113",
			"GH114",
			"GH115",
			"GH116",
			"GH117",
			"GH12",
			"GH120",
			"GH134",
			"GH121",
			"GH123",
			"GH124",
			"GH125",
			"GH126",
			"GH95",
			"GH128",
			"GH129",
			"GH13",
			"GH13_1",
			"GH13_10",
			"GH13_11",
			"GH13_12",
			"GH13_13",
			"GH13_14",
			"GH13_15",
			"GH13_16",
			"GH13_17",
			"GH13_18",
			"GH13_19",
			"GH13_2",
			"GH13_20",
			"GH13_21",
			"GH13_23",
			"GH13_26",
			"GH13_27",
			"GH13_28",
			"GH13_29",
			"GH13_3",
			"GH13_30",
			"GH13_31",
			"GH13_32",
			"GH13_33",
			"GH13_36",
			"GH13_38",
			"GH43_36",
			"GH80",
			"GH13_39",
			"GH13_4",
			"GH13_40",
			"GH13_41",
			"GH13_42",
			"GH13_5",
			"GH13_6",
			"GH13_7",
			"GH13_8",
			"GH13_9",
			"GH130",
			"GH133",
			"GH135",
			"GH136",
			"GH137",
			"GH138",
			"GH139",
			"GH140",
			"GH141",
			"GH142",
			"GT104",
			"GH22",
			"GH144",
			"GH145",
			"GH15",
			"GH16",
			"GH17",
			"GH18",
			"GH19",
			"GH2",
			"PL1_2",
			"GH23",
			"GH24",
			"GH25",
			"GH26",
			"GH27",
			"GH28",
			"GH29",
			"GH3",
			"GH30",
			"GH30_1",
			"GH30_2",
			"GH30_4",
			"GH30_5",
			"GH30_6",
			"GH30_7",
			"GH30_8",
			"GH31",
			"GH32",
			"GH33",
			"GH35",
			"GH36",
			"GH37",
			"GH38",
			"GH39",
			"GH4",
			"GH42",
			"GH43",
			"GH43_1",
			"GH43_10",
			"GH43_11",
			"GH43_12",
			"GH43_14",
			"GH43_16",
			"GH43_17",
			"GH43_18",
			"GH43_34",
			"GH43_2",
			"GH43_20",
			"GH43_21",
			"GH43_22",
			"GH43_23",
			"GH98",
			"GH43_26",
			"GH43_27",
			"GH43_28",
			"GH43_29",
			"GH43_3",
			"GH43_30",
			"GH43_31",
			"GH43_32",
			"GH43_33",
			"GH43_19",
			"GH43_35",
			"GH43_37",
			"GH89",
			"GH43_5",
			"GH43_7",
			"GH43_8",
			"GH43_9",
			"GH44",
			"GH46",
			"GH48",
			"GH49",
			"GH5",
			"GH5_1",
			"GH5_10",
			"GH5_13",
			"GH5_18",
			"GH5_19",
			"GH5_2",
			"GH5_20",
			"GH5_21",
			"GH5_22",
			"GH5_25",
			"GH5_26",
			"GH5_28",
			"GH5_35",
			"GH5_36",
			"GH5_37",
			"GH5_38",
			"GH5_39",
			"GH5_4",
			"GH5_40",
			"GH5_41",
			"GH5_42",
			"GH5_44",
			"GH5_46",
			"GH5_48",
			"GH5_5",
			"GH5_7",
			"GH5_8",
			"GH5_9",
			"GH50",
			"GH51",
			"GH52",
			"GH53",
			"GH55",
			"GH57",
			"GH58",
			"GH59",
			"PL12_1",
			"GH64",
			"GH65",
			"GH66",
			"GH67",
			"GH68",
			"GH70",
			"GH71",
			"GH72",
			"GH73",
			"GH74",
			"GH75",
			"GH76",
			"GH77",
			"GH78",
			"GH79",
			"GH8",
			"GH81",
			"GH82",
			"CBM57",
			"GH85",
			"GH86",
			"GH87",
			"GH88",
			"GH101",
			"GH9",
			"GH91",
			"GH92",
			"GH93",
			"GH94",
			"GH143",
			"GH96",
			"GH97",
			"GH127",
			"GH99",
			"GT1",
			"GT10",
			"GT101",
			"GT102",
			"GT103",
			"GT21",
			"GT78",
			"GT11",
			"GT12",
			"GT13",
			"GT14",
			"GT17",
			"GT19",
			"GT2",
			"GT20",
			"GH84",
			"GT22",
			"GT23",
			"GT25",
			"GT26",
			"GT27",
			"GT28",
			"GT29",
			"GT3",
			"GT30",
			"GT31",
			"GT32",
			"GT33",
			"GT35",
			"GT38",
			"GT39",
			"GT4",
			"GT40",
			"GT41",
			"GT44",
			"GT45",
			"GT46",
			"GT5",
			"GT51",
			"GT52",
			"GT56",
			"GT57",
			"GT6",
			"GT60",
			"GT66",
			"GT69",
			"GT7",
			"GT70",
			"GT73",
			"GT74",
			"GT75",
			"GT76",
			"GT8",
			"GT80",
			"GT81",
			"GT82",
			"GT83",
			"GT84",
			"GT43",
			"GT87",
			"GT9",
			"GT90",
			"GT92",
			"GT93",
			"GT94",
			"GT97",
			"GT99",
			"PL1",
			"PL1_11",
			"GH106",
			"PL1_3",
			"PL1_4",
			"PL1_5",
			"PL1_6",
			"PL10",
			"PL10_1",
			"PL10_2",
			"PL11",
			"PL14_2",
			"PL11_2",
			"PL12",
			"GH63",
			"PL12_2",
			"PL12_3",
			"PL13",
			"PL14",
			"PL15",
			"PL7_3",
			"PL15_2",
			"PL17",
			"PL3_3",
			"PL1_10",
			"PL14_5",
			"PL17_1",
			"PL17_2",
			"PL2_1",
			"PL14_4",
			"PL14_1",
			"PL1_8",
			"PL1_7",
			"PL21",
			"PL22",
			"PL22_1",
			"PL22_2",
			"PL25",
			"PL18",
			"PL26",
			"PL27",
			"PL1_12",
			"PL3_1",
			"PL7_1",
			"PL1_9",
			"PL3_4",
			"PL4",
			"PL4_1",
			"PL5",
			"PL5_1",
			"PL6",
			"PL6_1",
			"PL6_2",
			"PL7",
			"PL7_4",
			"PL3_5",
			"PL8",
			"PL8_1",
			"PL8_2",
			"PL21_1",
			"PL8_3",
			"PL9",
			"PL9_1",
			"PL9_2",
			"PL9_3",
			"PL9_4"
]]
	y_train = train[["group"]]
	# training
	min_samples_leaf = range(3,20,1)
	min_samples_split = range(3,20,1)
	random_state= range(21,100,1)
	tune_list = []
	for a in min_samples_leaf:
	    for b in min_samples_split:
	        for c in random_state:
	            rfc = RandomForestClassifier(
	            	n_estimators = 500, 
	            	max_depth = 5, 
	            	min_samples_leaf = a,
	            	min_samples_split = b, 
	            	random_state = c
	            	)
	            rfc.fit(x_train, y_train.values.ravel())
	            scores = cross_val_score(rfc, x_train, y_train.values.ravel(), cv=5)
	            rfc_y_predict = rfc.predict(x_train)
	            y_predprob = rfc.predict_proba(x_train)[:, 1]
	            tune_list.append([a, b, c])
	            print("min_samples_split: %d" % a)
	            print("min_samples_leaf: %d" % b)
	            print("random_state: %d" % c)
	            print("accuracy score (CV): %f" % scores.mean())
	            print("accuracy score (All): %f" % rfc.score(x_train, y_train))
	print("Finish !")

def main():
	arg = read_arg()
	training(arg.input)

if __name__ == '__main__':
    main()
