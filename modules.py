{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f479cb00",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pytorch_lightning as pl\n",
    "class IBMPriceDataModule(pl.LightningDataModule):\n",
    "    \n",
    "    def __init__(\n",
    "        self,train_sequences, test_sequences, batch_size=8\n",
    "    ):\n",
    "        super().__init__()\n",
    "        self.train_sequences=train_sequences\n",
    "        self.test_sequences=test_sequences\n",
    "        self.batch_size=batch_size\n",
    "\n",
    "    def setup(self):\n",
    "        self.train_dataset = IBMDataset(self.train_sequences)\n",
    "        self.test_dataset=IBMDataset(self.test_sequences)\n",
    "        \n",
    "        \n",
    "    def train_dataloader(self):\n",
    "        return DataLoader(\n",
    "            self.train_dataset,\n",
    "            batch_size=self.batch_size,\n",
    "            shuffle=False,\n",
    "            num_workers=2\n",
    "        )\n",
    "    \n",
    "    def val_dataloader(self): # Validation dataloader, for validation purposes:\n",
    "        return DataLoader(\n",
    "            self.test_dataset,\n",
    "            batch_size=1,\n",
    "            shuffle=False,\n",
    "            num_workers=1\n",
    "        )\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "88806a96",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
