

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def regressaoLinear_calculo():
    for i in range(0, len(tudo)):
        model = LinearRegression().fit(meses, tudo[i])
        y_pred = model.predict(meses)
        print('Dados do teste: ', tudo[i], sep='\n')
        print('Dados da predição', y_pred, sep='\n')


def graficoTotal():
    plt.plot(meses, custoAlimentacao,
             marker=configGrafico[0][0], c=configGrafico[0][1])
    plt.plot(meses, custoVestuario,
             marker=configGrafico[1][0], c=configGrafico[1][1])
    plt.plot(meses, custoTransporte,
             marker=configGrafico[2][0], c=configGrafico[2][1])
    plt.legend(['Alimentação', 'Vestuário', 'Lazer'], loc=0)
    plt.show()


def regressao1():
    model = LinearRegression().fit(meses, custoAlimentacao)
    y_pred = model.predict(meses)
    plt.plot(meses, custoAlimentacao,
             marker=configGrafico[0][0], c=configGrafico[0][1])
    plt.plot(meses, y_pred, c="g")
    plt.legend(['Alimentacao', 'previsão'], loc=0)
    plt.show()


def regressao2():
    model = LinearRegression().fit(meses, custoVestuario)
    z_pred = model.predict(meses)
    plt.plot(meses, custoVestuario,
             marker=configGrafico[1][0], c=configGrafico[1][1])
    plt.plot(meses, z_pred, c="g")
    plt.legend(['Vestuário', 'previsão'], loc=0)
    plt.show()


def regressao3():

    model = LinearRegression().fit(meses, custoTransporte)
    w_pred = model.predict(meses)
    plt.plot(meses, custoTransporte,
             marker=configGrafico[2][0], c=configGrafico[2][1])
    plt.plot(meses, w_pred, c="g")
    plt.legend(['Transporte', 'previsão'], loc=0)
    plt.show()


custoAlimentacao = np.array([15, 22, 14, 23, 20, 21])
custoVestuario = np.array([10, 26, 19, 24, 30, 24])
custoTransporte = np.array([30, 9, 4, 20, 2, 12])
configGrafico = (['o', 'red'], ['X', 'blue'], ['D', 'black'])

tudo = ([custoAlimentacao, custoVestuario, custoTransporte])
meses = []
tamanhoMes = len(tudo[0])
for i in range(len(tudo)):
    if len(tudo[i]) > tamanhoMes:
        tamanhoMes = len(tudo[i])

meses = np.arange(1, tamanhoMes+1)
meses = np.array(meses.reshape(-1, 1))

regressaoLinear_calculo()
graficoTotal()

regressao1()
regressao2()
regressao3()
