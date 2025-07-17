from domain.Borrow import Borrow
from domain.Rental import Rental 
from repository.BorrowRepository import BorrowRepository
from repository.DvdRepository import DvdRepository
from domain.Dvd import Dvd
from controller.Controller import Controller
from ui.UI import UI
import os

def main():
    # Ensure data files exist
    for filename in ["borrow.txt", "dvd.txt"]:
        if not os.path.exists(filename):
            with open(filename, "w"): pass
    BorrowRepo = BorrowRepository("borrow.txt")
    DvdRepo = DvdRepository("dvd.txt")
    
    ctrl = Controller(BorrowRepo,DvdRepo) 
    ui = UI(ctrl)
    ui.run()
    
main()