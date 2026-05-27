import MainLayout from "../layouts/MainLayout";
import { api } from "../api/axios";

const UploadPage = () => {

  const uploadFile = async (e) => {

    const file = e.target.files[0];

    const formData = new FormData();

    formData.append("file", file);

    try {

      await api.post(
        "/ingestion/sap/upload/",
        formData
      );

      alert("Upload Successful");

    } catch (error) {

      console.log(error);

      alert("Upload Failed");
    }
  };

  return (
    <MainLayout>

      <h1 className="text-4xl font-bold mb-8">
        Upload ESG Data
      </h1>

      <div className="bg-slate-900 rounded-2xl p-10">

        <input
          type="file"
          onChange={uploadFile}
        />

      </div>

    </MainLayout>
  );
};

export default UploadPage;