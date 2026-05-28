// import { useState } from 'react'

// import { uploadSapFile } from '../api/ingestionApi'


// export default function UploadCard() {

//   const [file, setFile] = useState(null)

//   const [message, setMessage] = useState('')


//   const handleUpload = async () => {

//     if (!file) return

//     try {

//       const data = await uploadSapFile(file)

//       setMessage(data.message)

//     } catch (error) {

//       setMessage('Upload failed')
//     }
//   }


//   return (
//     <div className="bg-white p-6 rounded-2xl shadow">

//       <h2 className="text-xl font-bold mb-4">
//         SAP Upload
//       </h2>

//       <input
//         type="file"
//         onChange={(e) => setFile(e.target.files[0])}
//       />

//       <button
//         onClick={handleUpload}
//         className="bg-black text-white px-4 py-2 rounded mt-4"
//       >
//         Upload
//       </button>

//       <p className="mt-4 text-green-600">
//         {message}
//       </p>

//     </div>
//   )
// }