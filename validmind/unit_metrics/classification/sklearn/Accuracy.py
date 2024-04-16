# Copyright © 2023-2024 ValidMind Inc. All rights reserved.
# See the LICENSE file in the root of this repository for details.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

from sklearn.metrics import accuracy_score

__tags = ["classification", "accuracy"]
__task_types = ["classification"]

__hello = "world"


@tags("classification", "accuracy")
@task_types("classification")
def Accuracy(dataset, model):
    """Calculates the accuracy of a model"""
    return accuracy_score(dataset.y, dataset.y_pred(model))
