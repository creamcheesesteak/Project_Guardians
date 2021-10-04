import pandas as pd
import sqlite3



class Co2:
    # c1 -> 개선 활동
    def c1(self,ind):
        con = sqlite3.connect('./sorting.db')

        df = pd.read_sql_query('select * from sorting',con)
        df2 = df[['industry','act','money','deco2']]
        df3 = df2[df2['industry'] == ind]

        result = df3['act'].tolist()
        return result

    # c2 -> 산업명
    def c2(self,ind):
        con = sqlite3.connect('./sorting.db')
        df = pd.read_sql_query('select * from sorting',con)
        df2 = df[['sort','industry']]
        df3 = df2[df2['industry'] == ind]

        result = df3['sort'].tolist()
        return result

    # c3 -> 절감액
    def c3(self,ind):
        con = sqlite3.connect('./sorting.db')
        df = pd.read_sql_query('select * from sorting',con)
        df2 = df[['industry','money']]
        df3 = df2[df2['industry'] == ind]

        result = df3['money'].tolist()
        return result

    # c4 -> 감축량
    def c4(self,ind):
        con = sqlite3.connect('./sorting.db')
        df = pd.read_sql_query('select * from sorting',con)
        df2 = df[['industry','deco2']]
        df3 = df2[df2['industry'] == ind]

        result = df3['deco2'].tolist()
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

    # test
    def sol1_alt(self,ind,user_co2):
        # django 돌릴때  경로
        con = sqlite3.connect('./sorting.db')
        # 테스트로 돌릴때  경로
        # con = sqlite3.connect('../../sorting.db')
        df = pd.read_sql_query('select * from top_8_final', con)
        df_manu = df[df['sort']=='제조업']
        df_bulid = df[df['sort']=='건설업']
        df_retail = df[df['sort']=='도매 및 소매업']
        df_mining = df[df['sort']=='광업']
        df_transport = df[df['sort']=='운수업']
        df_recycle = df[df['sort']=='폐기물 및 재생사업']
        df_energy = df[df['sort']=='전기, 가스, 증기 및 수도사업']
        df_primary = df[df['sort']=='농업, 임업 및 어업']
        user_co2 = float(user_co2)

        # 제조업
        if ind == 'manufacture':
            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_manu['deco2']:
                if i < user_co2:
                    data.append(i);
            for i in range(0,10):
                data2.append(data[i])
            for i in data2:
                df3 = df3.append(df_manu[df_manu['deco2']==i])

            df3 = df3.head(10)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 건설업
        elif ind == 'building':
            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_bulid['deco2']:
                if i < user_co2:
                    data.append(i);
            for i in range(0,10):
                data2.append(data[i])
            for i in data2:
                df3 = df3.append(df_bulid[df_bulid['deco2']==i])

            df3 = df3.head(10)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 도매 및 소매업
        elif ind == 'retail':
            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_retail['deco2']:
                if i < user_co2:
                    data.append(i);
            for i in range(0,10):
                data2.append(data[i])
            for i in data2:
                df3 = df3.append(df_retail[df_retail['deco2']==i])

            df3 = df3.head(10)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 광업
        elif ind == 'mining':
            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_mining['deco2']:
                if i < user_co2:
                    data.append(i);
            for i in range(0,10):
                data2.append(data[i])
            for i in data2:
                df3 = df3.append(df_mining[df_mining['deco2']==i])

            df3 = df3.head(10)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 운수업
        elif ind == 'transportation':
            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_transport['deco2']:
                if i < user_co2:
                    data.append(i);
            for i in range(0,10):
                data2.append(data[i])
            for i in data2:
                df3 = df3.append(df_transport[df_transport['deco2']==i])

            df3 = df3.head(10)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 폐기물 및 재생사업
        elif ind == 'recycle':
            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_recycle['deco2']:
                if i < user_co2:
                    data.append(i);
            for i in range(0,10):
                data2.append(data[i])
            for i in data2:
                df3 = df3.append(df_recycle[df_recycle['deco2']==i])

            df3 = df3.head(10)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 전기, 가스, 증기 및 수도사업
        elif ind == 'energy':
            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_energy['deco2']:
                if i < user_co2:
                    data.append(i);
            for i in range(0,10):
                data2.append(data[i])
            for i in data2:
                df3 = df3.append(df_energy[df_energy['deco2']==i])

            df3 = df3.head(10)
            result_data1 = df3['deco2'].tolist()
            result_data2 = df3['act'].tolist()
            result_data3 = df3['money'].tolist()

            result = result_data1 + result_data2 + result_data3

        # 농업, 임업 및 어업
        elif ind == 'primary':
            data = [];
            data2 = [];
            df3 = pd.DataFrame()


            for i in df_primary['deco2']:
                if i < user_co2:
                    data.append(i);
            for i in range(0,10):
                data2.append(data[i])
            for i in data2:
                df3 = df3.append(df_primary[df_primary['deco2']==i])

            df3 = df3.head(10)
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



