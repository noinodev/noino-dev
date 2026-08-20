if(!window.glInitialized) {
    window.glInitialized = true;
    window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('backdrop');
    const gl = canvas.getContext('webgl', { alpha: true });
    if (!gl) throw new Error('WebGL not supported');

    // resize canvas
    const resize = () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        gl.viewport(0, 0, canvas.width, canvas.height);
    };
    window.addEventListener('resize', resize);
    resize();

    // simple cube geometry
    const vertices = new Float32Array([
        -1,-1,1,  1,-1,1,  1,1,1, -1,1,1,
        -1,-1,-1, -1,1,-1,  1,1,-1, 1,-1,-1,
        -1,1,-1, -1,1,1, 1,1,1, 1,1,-1,
        -1,-1,-1, 1,-1,-1, 1,-1,1, -1,-1,1,
        1,-1,-1, 1,1,-1, 1,1,1, 1,-1,1,
        -1,-1,-1, -1,-1,1, -1,1,1, -1,1,-1
    ]);
    const indices = new Uint16Array([
        0,1,2,0,2,3, 4,5,6,4,6,7, 8,9,10,8,10,11,
        12,13,14,12,14,15,16,17,18,16,18,19,20,21,22,20,22,23
    ]);

    const vertexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

    const indexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer);
    gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indices, gl.STATIC_DRAW);

    // shaders
    const vsSource = `
        attribute vec3 position;
        uniform mat4 modelViewMatrix;
        uniform mat4 projectionMatrix;
        varying vec3 vDirection;
        void main() {
        vDirection = position;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
        }
    `;
    const fsSource = `
        precision mediump float;
        varying vec3 vDirection;
        uniform samplerCube skybox;
        void main() {
        gl_FragColor = textureCube(skybox, normalize(vDirection));
        }
    `;

    const createShader = (type, src) => {
        const shader = gl.createShader(type);
        gl.shaderSource(shader, src);
        gl.compileShader(shader);
        if(!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        throw new Error(gl.getShaderInfoLog(shader));
        }
        return shader;
    };

    const program = gl.createProgram();
    gl.attachShader(program, createShader(gl.VERTEX_SHADER, vsSource));
    gl.attachShader(program, createShader(gl.FRAGMENT_SHADER, fsSource));
    gl.linkProgram(program);

    const posLoc = gl.getAttribLocation(program, 'position');
    const mvLoc = gl.getUniformLocation(program, 'modelViewMatrix');
    const projLoc = gl.getUniformLocation(program, 'projectionMatrix');
    const skyLoc = gl.getUniformLocation(program, 'skybox');

    // cubemap loader
    const loadCubemap = path => {
        const tex = gl.createTexture();
        gl.bindTexture(gl.TEXTURE_CUBE_MAP, tex);

        const faces = [
        ['posx', gl.TEXTURE_CUBE_MAP_POSITIVE_X],
        ['negx', gl.TEXTURE_CUBE_MAP_NEGATIVE_X],
        ['posy', gl.TEXTURE_CUBE_MAP_POSITIVE_Y],
        ['negy', gl.TEXTURE_CUBE_MAP_NEGATIVE_Y],
        ['posz', gl.TEXTURE_CUBE_MAP_POSITIVE_Z],
        ['negz', gl.TEXTURE_CUBE_MAP_NEGATIVE_Z],
        ];

        faces.forEach(([name, target]) => {
        const img = new Image();
        img.src = `${path}/${name}.png`;
        img.onload = () => {
            gl.bindTexture(gl.TEXTURE_CUBE_MAP, tex);
            gl.texImage2D(target, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, img);
        };
        console.log(img);
        });

        gl.texParameteri(gl.TEXTURE_CUBE_MAP, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
        gl.texParameteri(gl.TEXTURE_CUBE_MAP, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
        gl.texParameteri(gl.TEXTURE_CUBE_MAP, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
        gl.texParameteri(gl.TEXTURE_CUBE_MAP, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
        return tex;
    };

    const cubemap = loadCubemap('/assets/images/pan'); // folder with posx.png etc.

    // math helpers
    const perspective = (fov, aspect, near, far) => {
        const f = 1 / Math.tan(fov/2);
        const nf = 1 / (near - far);
        return new Float32Array([
        f/aspect,0,0,0,
        0,f,0,0,
        0,0,(far+near)*nf,-1,
        0,0,2*far*near*nf,0
        ]);
    };

    const rotationMatrix = (x,y,z) => {
        const cx=Math.cos(x), sx=Math.sin(x);
        const cy=Math.cos(y), sy=Math.sin(y);
        const cz=Math.cos(z), sz=Math.sin(z);
        return new Float32Array([
        cy*cz,-cy*sz,sy,0,
        sx*sy*cz+cx*sz,-sx*sy*sz+cx*cz,-sx*cy,0,
        -cx*sy*cz+sx*sz,cx*sy*sz+sx*cz,cx*cy,0,
        0,0,0,1
        ]);
    };

    let time = 0;
    const render = () => {
        time += 0.002;

        gl.clearColor(0,0,0,0);
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
        gl.enable(gl.DEPTH_TEST);

        gl.useProgram(program);
        gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
        gl.enableVertexAttribArray(posLoc);
        gl.vertexAttribPointer(posLoc, 3, gl.FLOAT, false, 0, 0);
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer);

        const aspect = canvas.width / canvas.height;
        const proj = perspective(Math.PI/2, aspect, 0.1, 100);
        gl.uniformMatrix4fv(projLoc, false, proj);
        const mv = rotationMatrix(Math.sin(time*0.05)*0.1, time*0.04, 0);
        gl.uniformMatrix4fv(mvLoc, false, mv);

        gl.activeTexture(gl.TEXTURE0);
        gl.bindTexture(gl.TEXTURE_CUBE_MAP, cubemap);
        gl.uniform1i(skyLoc, 0);

        gl.drawElements(gl.TRIANGLES, 36, gl.UNSIGNED_SHORT, 0);

        requestAnimationFrame(render);
    };

    render();
    })();
}