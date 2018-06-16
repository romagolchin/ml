import sys

from PyQt5 import QtWidgets
from matplotlib import use

import model_selection_design

use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from model_selection import ModelSelector, score_funs


class App(QtWidgets.QMainWindow, model_selection_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        central_widget = self.centralWidget()
        layout = central_widget.layout()
        self.setCentralWidget(central_widget)

        fig = Figure()
        figure_size = (8, 20)
        fig.set_size_inches(*figure_size)
        fig.subplots_adjust(left=.2, top=.95, hspace=.7)
        self.canvas = FigureCanvas(fig)
        self.canvas.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding)
        scroll = QtWidgets.QScrollArea()
        scroll.setWidget(self.canvas)
        layout.addWidget(scroll)
        self.selectMetric.addItems(score_funs)
        self.btnGo.clicked.connect(self.run)
        self.model_selector = ModelSelector(self.canvas)

    def run(self):
        show_only_best = self.checkShowOnlyBest.isChecked()
        scorer = self.selectMetric.currentText()
        self.model_selector.show_only_best = show_only_best
        self.model_selector.scorer = scorer
        self.canvas.figure.clf()
        self.model_selector.select_model()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()

    app.exec_()


if __name__ == '__main__':
    main()
