from xlrd import open_workbook


class readDatatest:

    def dataTestLogin(self,url_data):
        data_test = open_workbook(url_data)

        values = []
        for s in data_test.sheets():
            # print 'Sheet:',s.name
            for row in range(1, s.nrows):
                col_names = s.row(0)
                col_value = []
                for name, col in zip(col_names, range(s.ncols)):
                    value = (s.cell(row, col).value)
                    try:
                        value = str(int(value))
                    except:
                        pass
                    col_value.append(value)
                values.append(col_value)
        return values
