import pandas as pd
import sqlite3



class Co2:


    # ind_name -> 산업명
    def ind_name(self,ind):
        con = sqlite3.connect('./sorting.db')
        df = pd.read_sql_query('select * from sorting',con)
        df2 = df[['sort','industry']]
        df3 = df2[df2['industry'] == ind]

        result = df3['sort'].tolist()
        return result


    # graph -> 그래프용 데이터 추출
    def graph(self,ind,sido):
        #df = pd.read_excel('../../data/calc2_result_graph.xlsx',engine='openpyxl', index_col=0);
        con = sqlite3.connect('./sorting.db')
        df = pd.read_sql_query('select * from calc2_result_graph',con)
        df = df.set_index('time')

        graph_col = ind + sido

        for i in df:
            if i == graph_col:
                df = df[graph_col]

        df2 = df.transpose()

        result = df2[['year_sum','tanso','tree']].tolist()
        return result

    ########################################################
    #---------------------BASE--------------------------------#
    # 감축량 이하값 기준으로 기본 sort (1순위 감축량 / 2순위 절감액)#
    ########################################################

    def sol1_alt(self,ind,user_co2):
        # django 돌릴때  경로
        con = sqlite3.connect('./sorting.db')
        # 테스트로 돌릴때  경로
        # con = sqlite3.connect('../../sorting.db')
        df = pd.read_sql_query('select * from top_8_final', con)

        user_co2 = float(user_co2)

        # 제조업
        if ind == 'manufacture':
            df_manu = df[df['sort'] == '제조업']

            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_manu['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_manu_except = df_manu.tail(5);
                df_manu_except2 = df_manu_except['deco2'].tolist();
                for i in df_manu_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_manu[df_manu['deco2']==i]);

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist();
            result_data2 = df3['act'].tolist();
            result_data3 = df3['money'].tolist();

            result = result_data1 + result_data2 + result_data3;

        # 건설업
        elif ind == 'building':
            df_bulid = df[df['sort'] == '건설업']

            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_bulid['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_bulid_except = df_bulid.tail(5);
                df_bulid_except2 = df_bulid_except['deco2'].tolist();
                for i in df_bulid_except2:
                    data2.append(i);


            for i in data2:
                df3 = df3.append(df_bulid[df_bulid['deco2']==i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 도매 및 소매업
        elif ind == 'retail':
            df_retail = df[df['sort'] == '도매 및 소매업']

            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_retail['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_retail_except = df_retail.tail(5);
                df_retail_except2 = df_retail_except['deco2'].tolist();
                for i in df_retail_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_retail[df_retail['deco2']==i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 광업
        elif ind == 'mining':
            df_mining = df[df['sort'] == '광업']

            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_mining['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_mining_except = df_mining.tail(5);
                df_mining_except2 = df_mining_except['deco2'].tolist();
                for i in df_mining_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_mining[df_mining['deco2']==i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 운수업
        elif ind == 'transportation':
            df_transport = df[df['sort'] == '운수업']

            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_transport['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_transport_except = df_transport.tail(5);
                df_transport_except2 = df_transport_except['deco2'].tolist();
                for i in df_transport_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_transport[df_transport['deco2']==i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 폐기물 및 재생사업
        elif ind == 'recycle':
            df_recycle = df[df['sort'] == '폐기물 및 재생사업']

            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_recycle['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_recycle_except = df_recycle.tail(5);
                df_recycle_except2 = df_recycle_except['deco2'].tolist();
                for i in df_recycle_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_recycle[df_recycle['deco2']==i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 발전에너지, 수도사업
        elif ind == 'energy':
            df_energy = df[df['sort'] == '발전에너지, 수도사업']

            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_energy['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_energy_except = df_energy.tail(5);
                df_energy_except2 = df_energy_except['deco2'].tolist();
                for i in df_energy_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_energy[df_energy['deco2']==i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 농림어업
        elif ind == 'primary':
            df_primary = df[df['sort'] == '농림어업']

            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_primary['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_primary_except = df_primary.tail(5);
                df_primary_except2 = df_primary_except['deco2'].tolist();
                for i in df_primary_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_primary[df_primary['deco2']==i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3


        return result
    ########################################################
    # 감축량 이하값 기준으로 sort (에너지 절감량(연료) 기준)#
    ########################################################

    def sol1_alt_fuel(self,ind,user_co2):
        # django 돌릴때  경로
        con = sqlite3.connect('./sorting.db')
        # 테스트로 돌릴때  경로
        # con = sqlite3.connect('../../sorting.db')
        df = pd.read_sql_query('select * from top_8_final', con)

        user_co2 = float(user_co2)

        # 제조업
        if ind == 'manufacture':
            df_manu = df[df['sort'] == '제조업']
            df_manu = df_manu.sort_values(by=['에너지 절감량(연료)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()



            for i in df_manu['deco2']:
                if i < user_co2:
                    data.append(i);
            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_manu_except = df_manu.tail(5);
                df_manu_except2 = df_manu_except['deco2'].tolist();
                for i in df_manu_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_manu[df_manu['deco2']==i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 건설업
        elif ind == 'building':
            df_bulid = df[df['sort'] == '건설업']
            df_bulid = df_bulid.sort_values(by=['에너지 절감량(연료)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_bulid['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_bulid_except = df_bulid.tail(5);
                df_bulid_except2 = df_bulid_except['deco2'].tolist();
                for i in df_bulid_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_bulid[df_bulid['deco2']==i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 도매 및 소매업
        elif ind == 'retail':
            df_retail = df[df['sort'] == '도매 및 소매업']
            df_retail = df_retail.sort_values(by=['에너지 절감량(연료)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_retail['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_retail_except = df_retail.tail(5);
                df_retail_except2 = df_retail_except['deco2'].tolist();
                for i in df_retail_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_retail[df_retail['deco2']==i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 광업
        elif ind == 'mining':
            df_mining = df[df['sort'] == '광업']
            df_mining = df_mining.sort_values(by=['에너지 절감량(연료)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_mining['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_mining_except = df_mining.tail(5);
                df_mining_except2 = df_mining_except['deco2'].tolist();
                for i in df_mining_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_mining[df_mining['deco2']==i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 운수업
        elif ind == 'transportation':
            df_transport = df[df['sort'] == '운수업']
            df_transport = df_transport.sort_values(by=['에너지 절감량(연료)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_transport['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_transport_except = df_transport.tail(5);
                df_transport_except2 = df_transport_except['deco2'].tolist();
                for i in df_transport_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_transport[df_transport['deco2']==i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 폐기물 및 재생사업
        elif ind == 'recycle':
            df_recycle = df[df['sort'] == '폐기물 및 재생사업']
            df_recycle = df_recycle.sort_values(by=['에너지 절감량(연료)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_recycle['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_recycle_except = df_recycle.tail(5);
                df_recycle_except2 = df_recycle_except['deco2'].tolist();
                for i in df_recycle_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_recycle[df_recycle['deco2']==i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 발전에너지, 수도사업
        elif ind == 'energy':
            df_energy = df[df['sort'] == '발전에너지, 수도사업']
            df_energy = df_energy.sort_values(by=['에너지 절감량(연료)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_energy['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_energy_except = df_energy.tail(5);
                df_energy_except2 = df_energy_except['deco2'].tolist();
                for i in df_energy_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_energy[df_energy['deco2']==i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 농림어업
        elif ind == 'primary':
            df_primary = df[df['sort'] == '농림어업']
            df_primary = df_primary.sort_values(by=['에너지 절감량(연료)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_primary['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_primary_except = df_primary.tail(5);
                df_primary_except2 = df_primary_except['deco2'].tolist();
                for i in df_primary_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_primary[df_primary['deco2']==i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3


        return result

    ########################################################
    # 감축량 이하값 기준으로 sort (에너지 절감량(전력) 기준)#
   ########################################################

    def sol1_alt_elec(self, ind, user_co2):
        # django 돌릴때  경로
        con = sqlite3.connect('./sorting.db')
        # 테스트로 돌릴때  경로
        # con = sqlite3.connect('../../sorting.db')
        df = pd.read_sql_query('select * from top_8_final', con)

        user_co2 = float(user_co2)

        # 제조업
        if ind == 'manufacture':
            df_manu = df[df['sort'] == '제조업']
            df_manu = df_manu.sort_values(by=['에너지 절감량(전력)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()

            for i in df_manu['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_manu_except = df_manu.tail(5);
                df_manu_except2 = df_manu_except['deco2'].tolist();
                for i in df_manu_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_manu[df_manu['deco2'] == i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 건설업
        elif ind == 'building':
            df_bulid = df[df['sort'] == '건설업']
            df_bulid = df_bulid.sort_values(by=['에너지 절감량(전력)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()

            for i in df_bulid['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_bulid_except = df_bulid.tail(5);
                df_bulid_except2 = df_bulid_except['deco2'].tolist();
                for i in df_bulid_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_bulid[df_bulid['deco2'] == i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 도매 및 소매업
        elif ind == 'retail':
            df_retail = df[df['sort'] == '도매 및 소매업']
            df_retail = df_retail.sort_values(by=['에너지 절감량(전력)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()

            for i in df_retail['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_retail_except = df_retail.tail(5);
                df_retail_except2 = df_retail_except['deco2'].tolist();
                for i in df_retail_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_retail[df_retail['deco2'] == i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 광업
        elif ind == 'mining':
            df_mining = df[df['sort'] == '광업']
            df_mining = df_mining.sort_values(by=['에너지 절감량(전력)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()

            for i in df_mining['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_mining_except = df_mining.tail(5);
                df_mining_except2 = df_mining_except['deco2'].tolist();
                for i in df_mining_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_mining[df_mining['deco2'] == i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 운수업
        elif ind == 'transportation':
            df_transport = df[df['sort'] == '운수업']
            df_transport = df_transport.sort_values(by=['에너지 절감량(전력)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()

            for i in df_transport['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_transport_except = df_transport.tail(5);
                df_transport_except2 = df_transport_except['deco2'].tolist();
                for i in df_transport_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_transport[df_transport['deco2'] == i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 폐기물 및 재생사업
        elif ind == 'recycle':
            df_recycle = df[df['sort'] == '폐기물 및 재생사업']
            df_recycle = df_recycle.sort_values(by=['에너지 절감량(전력)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()

            for i in df_recycle['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_recycle_except = df_recycle.tail(5);
                df_recycle_except2 = df_recycle_except['deco2'].tolist();
                for i in df_recycle_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_recycle[df_recycle['deco2'] == i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 발전에너지, 수도사업
        elif ind == 'energy':
            df_energy = df[df['sort'] == '발전에너지, 수도사업']
            df_energy = df_energy.sort_values(by=['에너지 절감량(전력)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()

            for i in df_energy['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_energy_except = df_energy.tail(5);
                df_energy_except2 = df_energy_except['deco2'].tolist();
                for i in df_energy_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_energy[df_energy['deco2'] == i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 농림어업
        elif ind == 'primary':
            df_primary = df[df['sort'] == '농림어업']
            df_primary = df_primary.sort_values(by=['에너지 절감량(전력)'], ascending=[False])

            data = [];
            data2 = [];
            df3 = pd.DataFrame()

            for i in df_primary['deco2']:
                if i < user_co2:
                    data.append(i);

            try:
                for i in range(0,5):
                    data2.append(data[i]);
            except:
                df_primary_except = df_primary.tail(5);
                df_primary_except2 = df_primary_except['deco2'].tolist();
                for i in df_primary_except2:
                    data2.append(i);

            for i in data2:
                df3 = df3.append(df_primary[df_primary['deco2'] == i])

            df3 = df3.head(5)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        return result





if __name__ == '__main__':
     # print(Co2().c1('manufacture'))
     # print(Co2().c3('manufacture'))
     # print(Co2().graph('manufacture','강원도'))
     print(Co2().sol1_alt('primary',40))
     print(Co2().sol1_alt_fuel('primary',40))
     print(Co2().sol1_alt_elec('primary',40))



