import matplotlib.pyplot as plt

def plot_data(real, predicted=None):
    plt.figure(figsize=(8,5))
    plt.plot(real, label="Température réelle", marker="o")
    if predicted is not None:
        plt.plot(range(len(real), len(real)+len(predicted)), predicted, 
                 label="Prévisions", marker="x")
    plt.xlabel("Temps")
    plt.ylabel("Température (°C)")
    plt.legend()
    plt.title("Visualisation des données SmartPredict")
    plt.show()

if __name__ == "__main__":
    real_data = [20.5, 21.0, 21.2, 22.0, 22.5]
    predicted = [23.0, 23.5, 24.0]
    plot_data(real_data, predicted)
