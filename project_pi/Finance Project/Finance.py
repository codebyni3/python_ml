from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, f1_score
import matplotlib.pyplot as plt

y_true = [1]*100 + [0]*100
y_pred = [1]*90 + [0]*10 + [0]*80 + [1]*20

f1_score= accuracy_score(y_true, y_pred)
print(f"Accuracy: {f1_score* 100:.2f}%")

cm = confusion_matrix(y_true, y_pred, labels=[1, 0])
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Disease", "No Disease"])
disp.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.show()
