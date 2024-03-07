class Product:
    def __init__(self, name, price, amount, productDemand, leadTime, deliveryTime) -> None:
        self.name = name
        self.price = price
        self.amount = amount
        #Safety stock to prevent your product storage from running out
        #Estoque de segurança para evitar que seu armazenamento de produtos fique zerado 
        safetyStock = deliveryTime * productDemand
        #Reorder Point | Ponto de Ressuprimento
        self.reorderPoint = productDemand * leadTime + safetyStock

class Department:
    def __init__(self, name) -> None:
        self.name = name

    def update(self):
        print(self.name + " department notified")

class Stock:
    departments = [] 
    products = []

    def subscrive(self, department: Department) -> None:
        self.departments.append(department)

    def unsubscrive(self, department: Department) -> None:
        self.departments.remove(department)

    def notify(self) -> None:
        for department in self.departments:
            department.update()

    def addProduct(self, product: Product) -> None:
        self.products.append(product)

    def removeProduct(self, product: Product) -> None:
        self.products.remove(product)
        
    def buyProduct(self, product, amount):
        index = self.products.index(product)
        if(self.products[index].amount >= amount):
            self.products[index].amount -= amount
            if(self.products[index].amount <= self.products[index].reorderPoint):
                print("Reorder Point reached, notifying observers")
                self.notify()
        else:
            print("Quantity unavailable, we only have " + str(self.products[index].amount) + " units in stock")

if __name__ == "__main__":

    subject = Stock()

    purchasing = Department("Purchasing")
    subject.subscrive(purchasing)

    marketing = Department("Marketing")
    subject.subscrive(marketing)

    css = Department("Customer Support System")
    subject.subscrive(css)

    product = Product("Mouse", 60, 100, 10, 1, 1)
    subject.addProduct(product)

    subject.buyProduct(product, 180)
    subject.buyProduct(product, 20)
    subject.buyProduct(product, 60)