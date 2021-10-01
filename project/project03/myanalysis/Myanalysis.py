import pandas as pd
import sqlite3
from project.config.settings import DATA_DIRS


class Co2:
    # c1 -> 개선 활동
    def c1(self,ind):
        connect = sqlite3.connect(DATA_DIRS[0]+'\\sorting.db')

        df = pd.read_sql_query('select * from sorting',connect)
        df2 = df[['industry','act','money','deco2']]
        df3 = df2[df2['industry'] == ind]

        result = df3['act'].tolist()
        return result

    # c2 -> 산업명
    def c2(self,ind):
        connect = sqlite3.connect(DATA_DIRS[0]+'\\sorting.db')
        df = pd.read_sql_query('select * from sorting',connect)
        df2 = df[['sort','industry']]
        df3 = df2[df2['industry'] == ind]

        result = df3['sort'].tolist()
        return result

    # c3 -> 절감액
    def c3(self,ind):
        connect = sqlite3.connect(DATA_DIRS[0]+'\\sorting.db')
        df = pd.read_sql_query('select * from sorting',connect)
        df2 = df[['industry','money']]
        df3 = df2[df2['industry'] == ind]

        result = df3['money'].tolist()
        return result

    # c4 -> 감축량
    def c4(self,ind):
        connect = sqlite3.connect(DATA_DIRS[0]+'\\sorting.db')
        df = pd.read_sql_query('select * from sorting',connect)
        df2 = df[['industry','deco2']]
        df3 = df2[df2['industry'] == ind]

        result = df3['deco2'].tolist()
        return result

    # graph -> 그래프용 데이터 추출
    def graph(self,ind,sido):
        #df = pd.read_excel('../../data/calc2_result_graph.xlsx',engine='openpyxl', index_col=0);
        connect = sqlite3.connect(DATA_DIRS[0]+'\\sorting.db')
        df = pd.read_sql_query('select * from calc2_result_graph',connect)
        df = df.set_index('time')

        graph_col = ind + sido

        for i in df:
            if i == graph_col:
                df = df[graph_col]

        df2 = df.transpose()

        result = df2[['year_sum','tanso','tree']].tolist()
        return result



if __name__ == '__main__':
     print(Co2().c1('manufacture'))
     print(Co2().c3('manufacture'))
     print(Co2().graph('manufacture','강원도'))


