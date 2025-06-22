from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Sample true and predicted labels
y_true = [1]*100 + [0]*100
y_pred = [1]*90 + [0]*10 + [0]*80 + [1]*20

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:\n", cm)

# Other Metrics
print("Accuracy:", accuracy_score(y_true, y_pred))
print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1 Score:", f1_score(y_true, y_pred))
