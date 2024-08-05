import numpy as np
import matplotlib.pyplot as plt
import h5py
import os

class HDF5Handler:
    def __init__(self, file_path):
        self.file_path = file_path

    def print_structure(self):
        """Prints the structure of the HDF5 file."""
        def print_keys(name, obj):
            print(name)
        
        with h5py.File(self.file_path, "r") as f:
            f.visititems(print_keys)

    def read_data(self, dataset_path, indices):
        """Reads data from the specified dataset path in the HDF5 file and stores it in the instance."""
        with h5py.File(self.file_path, "r") as f:
            self.data = f[dataset_path][:]
        
        data = self.data[indices]
        
        return data

    def plot_1d_data(self, x, y, x_label = "X Axis", y_label = "Y Axis", title = "X vs Y Data"):
        """Plots the 1D data if it has been read."""
        plt.figure()
        plt.plot(x, y, 'o')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()

    def save_1d_data_to_txt(self, x, y, output_file, x_axis = "X Axis", y_axis = "Y Axis"):
        """Saves the 1D data to a TXT file."""      
        combined_data = np.column_stack((x, y))
        header = x_axis + "\t" + y_axis
        np.savetxt(output_file, combined_data, fmt="%.18e", delimiter="\t", header=header)

if __name__ == "__main__":
    folder_name = os.path.dirname(os.path.abspath(__file__))
    file_name = "0008-SNR_woPump_highField_231p562mT_PSG_6.86103_GHz_202407290008.hdf5"
    file_path = os.path.join(folder_name, file_name)
    file_name_txt = "txt_file.txt"
    dataset_path = "Data/Data"  # Modify this path as needed

    handler = HDF5Handler(file_path)

    # 1. Print the structure of the HDF5 file
    handler.print_structure()

    # 2. Return x and y values for the 1D plot (assuming data is in a shape like self.data[:, x_index, z_index] or other variants)
    x = handler.read_data(dataset_path, indices=(slice(None),0,10))
    y = handler.read_data(dataset_path, indices=(slice(None),2,10))
    
    # 3. Show the 1D plot
    handler.plot_1d_data(x, y)

    # 4. Save to a TXT file
    handler.save_1d_data_to_txt(x, y, os.path.join(folder_name, file_name_txt))
