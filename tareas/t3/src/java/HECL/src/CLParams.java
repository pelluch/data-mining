
import com.jogamp.opencl.CLCommandQueue;
import com.jogamp.opencl.CLContext;
import com.jogamp.opencl.CLDevice;
import com.jogamp.opencl.CLKernel;
import com.jogamp.opencl.CLProgram;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;


public class CLParams {
	private String kernelFile;
	private CLProgram program;
	private CLContext context;
	private CLCommandQueue queue;
	private CLDevice device;
	private Map<String, CLKernel> kernels;
	
	public CLContext getContext(){
		return context;
	}
	
	public CLCommandQueue getQueue(){
		return queue;
	}
	
	public int getMaxWorkGroupSize()
	{
		if(device != null)
			return device.getMaxWorkGroupSize();
		
		return 0;
	}
	
	public CLParams(String kernelFile){
		this.kernelFile = kernelFile;
		this.kernels = new HashMap<String, CLKernel>();
	}
	
	public CLKernel getKernel(String kernelName) {
		if(kernels.containsKey(kernelName))
			return kernels.get(kernelName);
		
		return null;	
	}

	public void init() throws IOException
	{
		// set up (uses default CLPlatform and creates context for all devices)
        context = CLContext.create();
        
        // select fastest device
        device = context.getMaxFlopsDevice();

        // create program and initialize the kernels Map
        program = context.createProgram(CLParams.class.getResourceAsStream(kernelFile)).build();
        kernels = program.createCLKernels();
        
        queue = device.createCommandQueue();
	}
	
	public void release()
	{
        context.release();
	}
}
